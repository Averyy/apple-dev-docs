# enhanceDocuments

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that enhances the documents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var enhanceDocuments: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reader` domain and one of your app’s actions matches the `enhanceDocuments` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .reader.enhanceDocuments)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `enhanceDocuments` schema:

```swift
@AppIntent(schema: .reader.enhanceDocuments)
struct ReaderEnhanceDocumentsIntent {
    var target: [<#ReaderDocumentEntity#>]

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Actions
- [var deletePages: some AppSchemaIntent](./deletepages.md)
  An intent schema that deletes the specified pages.
- [var insertPages: some AppSchemaIntent](./insertpages.md)
  An intent schema that inserts pages from the specified files.
- [var openDocument: some AppSchemaIntent](./opendocument.md)
  An intent schema that opens the specified files in the reader.
- [var openPage: some AppSchemaIntent](./openpage.md)
  An intent schema that opens the app to the specified document page.
- [var resizeDocuments: some AppSchemaIntent](./resizedocuments.md)
  An intent schema that resizes the documents to a particular width and height.
- [var rotateDocuments: some AppSchemaIntent](./rotatedocuments.md)
  An intent schema that rotates the documents in the specified direction.
- [var rotatePages: some AppSchemaIntent](./rotatepages.md)
  An intent schema that rotates the pages in the specified direction.
- [var searchDocuments: some AppSchemaIntent](./searchdocuments.md)
  An intent schema that searches for text in the documents.
- [AppSchema.ReaderIntent](../readerintent.md)
  Identifies intent schemas in the reader domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerintent/enhancedocuments)*