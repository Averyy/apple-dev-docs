# Getting started with StateReporting

**Framework**: StateReporting

Define reportable metadata types, obtain a state reporter for your domain, and report transitions at the right call sites in your app.

#### Overview

StateReporting helps track the states your app moves through during use, giving diagnostic tools the context to attribute performance metrics to specific features and conditions. Each state is identified by a string label you provide when reporting a transition, along with optional structured metadata. You define the domains and states that make sense for your app, obtain a reporter for each domain, and report transitions at the right call sites.

To begin using StateReporting, link the framework to your app target and call the API at state transitions. From there, diagnostic tools like [`MetricKit`](https://developer.apple.com/documentation/metrickit) and Instruments surface your reported state in their reports. Use those reports to attribute performance metrics to the specific features and states in your app.

#### Define a State Reporter

Call [`reporter(for:stableMetadata:volatileMetadata:)`](statereporter/reporter(for:stablemetadata:volatilemetadata:).md) with a domain string to get an instance. Pass the metadata types for your stable and volatile metadata. Store the reporter in a long-lived object — such as a scene manager, view model, or app delegate — so it persists for the lifetime of the domain. [`StateReporter`](statereporter.md) returns the same instance for a given domain on every call.

In the following example, `GraphicsSettings` and `GameplayVolatileMetadata` are reportable metadata types you define — see [`Define reportable metadata`](getting-started-with-statereporting#Define-reportable-metadata.md).

```swift
// Get the dedicated reporter instance for the gameplay domain.
let gameplayReporter = StateReporter.reporter(
    for: "com.mygame.gameplay",
    stableMetadata: GraphicsSettings.self,
    volatileMetadata: GameplayVolatileMetadata.self
)
```

> ⚠️ **Warning**: Calling [`reporter(for:stableMetadata:volatileMetadata:)`](statereporter/reporter(for:stablemetadata:volatilemetadata:).md) for the same domain with different metadata types crashes at runtime. Decide on your metadata types before shipping. Treat them as stable across your codebase.

#### Report State Transitions

Call [`reportTransition(to:stableMetadata:volatileMetadata:)`](statereporter/reporttransition(to:stablemetadata:volatilemetadata:).md) when your app moves to a new state. Pass the new label, updated stable metadata, and current volatile metadata. StateReporting records a transition only when the label or stable metadata changes.

```swift
// Report starting gameplay with both stable and volatile metadata.
gameplayReporter.reportTransition(
    to: "Playing",
    stableMetadata: GraphicsSettings(graphicsQuality: "High", engineVersion: "1.2.3"),
    volatileMetadata: GameplayVolatileMetadata(playerHealth: 100)
)
```

Pass `nil` as the label to clear the active state entirely, and omit the optional metadata parameters. Passing an empty string triggers a fatal error.

```swift
func endLevel() {
    gameplayReporter.reportTransition(to: nil)
}
```

Call [`reportVolatileMetadataUpdate(_:)`](statereporter/reportvolatilemetadataupdate(_:).md) to update volatile metadata without triggering a new transition. This call has no effect if no state is currently active.

```swift
// Update volatile metadata as gameplay progresses
gameplayReporter.reportVolatileMetadataUpdate(
    GameplayVolatileMetadata(playerHealth: 75)
)
```

> ❗ **Important**: StateReporting applies a rate limit. Call [`reportTransition(to:stableMetadata:volatileMetadata:)`](statereporter/reporttransition(to:stablemetadata:volatilemetadata:).md) and [`reportVolatileMetadataUpdate(_:)`](statereporter/reportvolatilemetadataupdate(_:).md) at human-interaction timescales, such as when you tap a button, navigate to a new screen, or start an activity. Calling them on every frame or in a tight loop causes StateReporting to drop data.

#### Choose Your Domains and States

A domain is a reverse-DNS string that identifies one functional area of your app, such as `"com.mygame.gameplay"` or `"com.myapp.checkout"`. The system creates a reporter instance unique to the domain on first use. The type parameters you supply at that point persist for the lifetime of the process. Choose domain strings that are stable across app versions. Changing a domain string starts a new data series under the new name, and data recorded under the old domain string does not correlate with the new series.

At most one state is active per domain at a time. Each state has a *label* (a short string like `"High"` or `"Low"`) and optional structured metadata. Keep the number of distinct states small. For example, a game graphics settings domain might use fixed labels like `"Low"`, `"Medium"`, `"High"`, and `"Ultra"`.

Avoid embedding dynamic values directly in a label or stable metadata string, as diagnostic tools aggregate metrics for each unique combination of label and stable metadata. A value like `"Score-\(score)"` creates a distinct state for every value of `score`, fragmenting your data into buckets too small to be meaningful. Prefer a small, fixed set of labels like `"Low"`, `"Medium"`, and `"High"`, and encode the raw value in the volatile metadata.

#### Use Statereporting in App Extensions

You can call [`reporter(for:stableMetadata:volatileMetadata:)`](statereporter/reporter(for:stablemetadata:volatilemetadata:).md) from an app extension, using the same pattern as in your main app. Create or obtain a reporter for the appropriate domain, then call [`reportTransition(to:stableMetadata:volatileMetadata:)`](statereporter/reporttransition(to:stablemetadata:volatilemetadata:).md) at state transitions within the extension.

Because metric data isn’t available for app extensions, state transitions emitted from an extension don’t appear in a [`MetricReport`](https://developer.apple.com/documentation/metrickit/metricreport).

Diagnostic reports can include extension state. States emitted by the extension appear in [`states`](https://developer.apple.com/documentation/metrickit/diagnosticreport/environment-swift.struct/states), giving diagnostic tools the full state context at the time of the event. The system delivers diagnostic reports to the main app, not the extension itself.

The extension must register its domains with [`MetricManager`](https://developer.apple.com/documentation/metrickit/metricmanager) directly. Create a `MetricManager` instance within the extension and pass the relevant domains to [`enabledStateReportingDomains`](https://developer.apple.com/documentation/metrickit/metricmanager/enabledstatereportingdomains). The extension must both register its domains and emit states and signposts.

#### Define Reportable Metadata

[`ReportableMetadata`](reportablemetadata.md) is a protocol that requires a `metadataDictionary` property returning `[String: ReportableMetadataValue]`. Rather than implementing this manually, apply the [`ReportableMetadata()`](reportablemetadata().md) macro, which generates this conformance automatically.

**Stable metadata** provides the context for categorization. Keep the number of distinct values small. In a game, the graphics quality setting and engine version are good candidates.

```swift
import StateReporting

@ReportableMetadata
struct GraphicsSettings {
    let graphicsQuality: String
    let engineVersion: String
}
```

Use **volatile metadata** to annotate the active state with data that changes within it, without triggering a transition. This gives diagnostic tools finer-grained context. For example, if performance diagnostics show unresponsive intervals during “Playing”, use volatile metadata to correlate those intervals with game conditions like low player health. Volatile metadata does not affect aggregation in downstream tools.

```swift
@ReportableMetadata
struct GameplayVolatileMetadata {
    let playerHealth: Int
}
```

Use [`ReportableMetadataKey(_:)`](reportablemetadatakey(_:).md) to specify a custom key name for a property in the metadata dictionary when you want a shorter or more stable key than the property name. Use [`ReportableMetadataIgnored()`](reportablemetadataignored().md) to exclude a property entirely, such as an internal tracking value that’s not relevant to performance analysis.

The following version of `GraphicsSettings` adds two properties that demonstrate each macro:

```swift
@ReportableMetadata
struct GraphicsSettings {
    let graphicsQuality: String
    let engineVersion: String
    @ReportableMetadataKey("api") let graphicsAPIName: String
    @ReportableMetadataIgnored let localCacheID: String
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/getting-started-with-statereporting)*