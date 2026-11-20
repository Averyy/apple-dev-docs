# open

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens an item in the application.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var open: some AppSchemaIntent { get }
```

## Mentions

- [Presenting an entity as a card snippet](../../presenting-an-entity-as-a-card-snippet.md)

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `system` domain and one of your app’s actions matches the `open` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .system.open)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `open` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `system_open` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .system.open)
struct SystemOpenIntent: OpenIntent {
    /// Item to open.
    var target: <#any AppEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the open intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `any AppEntity` | Your app | Item to open. |

## See Also

### Actions
- [var searchInApp: some AppSchemaIntent](./searchinapp.md)
  An intent schema that navigates to search results.
- [AppSchema.SystemIntent](../systemintent.md)
  Identifies intent schemas in the system domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/systemintent/open)*