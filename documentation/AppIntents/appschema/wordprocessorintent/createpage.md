# createPage

**Framework**: App Intents  
**Kind**: property

An intent schema that creates a new page in an editor document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var createPage: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `wordProcessor` domain and one of your app’s actions matches the `createPage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .wordProcessor.createPage)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createPage` schema:

```swift
@AppIntent(schema: .wordProcessor.createPage)
struct CreateWordProcessorPageIntent {
    var target: <#WordProcessorDocumentEntity#>
    var template: String?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var addAudioToPage: some AppSchemaIntent](appschema/wordprocessorintent/addaudiotopage.md)
  An intent schema that adds an audio clip to a page.
- [var addImageToPage: some AppSchemaIntent](appschema/wordprocessorintent/addimagetopage.md)
  An intent schema that adds an image to a page.
- [var addTextBoxToPage: some AppSchemaIntent](appschema/wordprocessorintent/addtextboxtopage.md)
  An intent schema that adds a textbox to a page.
- [var addVideoToPage: some AppSchemaIntent](appschema/wordprocessorintent/addvideotopage.md)
  An intent schema that adds a video to a page.
- [var addWebVideoToPage: some AppSchemaIntent](appschema/wordprocessorintent/addwebvideotopage.md)
  An intent schema that adds a web video to a page.
- [var create: some AppSchemaIntent](appschema/wordprocessorintent/create.md)
  An intent schema that opens the app for composing a new text document.
- [var open: some AppSchemaIntent](appschema/wordprocessorintent/open.md)
  An intent schema that opens the app to an editor.
- [var openPage: some AppSchemaIntent](appschema/wordprocessorintent/openpage.md)
  An intent schema that opens an editor document page.
- [AppSchema.WordProcessorIntent](appschema/wordprocessorintent.md)
  Identifies intent schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorintent/createpage)*