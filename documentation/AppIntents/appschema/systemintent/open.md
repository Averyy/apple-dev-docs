# open

**Framework**: App Intents  
**Kind**: property

An intent schema that opens an item in the application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var open: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `system` domain and one of your app’s actions matches the `open` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .system.open)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `open` schema:

```swift
@AppIntent(schema: .system.open)
struct OpenIntent: OpenIntent {
    var target: <#any AppEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var search: some AppSchemaIntent](appschema/systemintent/search.md)
  An intent schema that navigates to search results.
- [AppSchema.SystemIntent](appschema/systemintent.md)
  Identifies intent schemas in the system domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/systemintent/open)*