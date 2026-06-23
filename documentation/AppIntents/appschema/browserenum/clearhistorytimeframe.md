# clearHistoryTimeFrame

**Framework**: App Intents  
**Kind**: property

An enum schema for a clear history time frame parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var clearHistoryTimeFrame: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `browser` domain and a parameter type matches the `clearHistoryTimeFrame` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .browser.clearHistoryTimeFrame)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `clearHistoryTimeFrame` schema:

```swift
@AppEnum(schema: .browser.clearHistoryTimeFrame)
enum ClearHistoryTimeFrameEnum: String {
    case <#ClearHistoryTimeFrameEnum Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [AppSchema.BrowserEnum](appschema/browserenum.md)
  Identifies enum schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserenum/clearhistorytimeframe)*