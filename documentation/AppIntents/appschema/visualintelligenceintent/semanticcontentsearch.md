# semanticContentSearch

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that shows more and richer visual search results in the app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 27.0+

## Declaration

```swift
var semanticContentSearch: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `visualIntelligence` domain and one of your app’s actions matches the `semanticContentSearch` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .visualIntelligence.semanticContentSearch)` Swift macro.

The following example shows an intent that conforms to the `semanticContentSearch` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `visualIntelligence_semanticContentSearch` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .visualIntelligence.semanticContentSearch)
struct ShowVisualSearchResultsInAppIntent {
    /// Semantic content to be saved.
    var semanticContent: VisualIntelligence.SceneDescriptor

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts
- Visual Intelligence

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the semantic-content-search intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `semanticContent` | `VisualIntelligence.SceneDescriptor` | VisualIntelligence | Semantic content to be saved. |

## See Also

### Actions
- [AppSchema.VisualIntelligenceIntent](../visualintelligenceintent.md)
  Identifies intent schemas in the visual intelligence domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/visualintelligenceintent/semanticcontentsearch)*