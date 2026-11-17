# openPage

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens the app to the specified document page.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var openPage: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reader` domain and one of your app’s actions matches the `openPage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .reader.openPage)` Swift macro.

The following example shows an intent that conforms to the `openPage` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reader_openPage` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .reader.openPage)
struct ReaderOpenPageIntent: OpenIntent {
    /// Page to go to.
    var target: <#ReaderPageEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the open-page intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .reader.page)` | Your app | Page to go to. `ReaderPageEntity` is a placeholder name for a type that conforms to the [`page`](../readerentity/page.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var deletePages: some AppSchemaIntent](./deletepages.md)
  An intent schema that deletes the specified pages.
- [var enhanceDocuments: some AppSchemaIntent](./enhancedocuments.md)
  An intent schema that enhances the documents.
- [var insertPages: some AppSchemaIntent](./insertpages.md)
  An intent schema that inserts pages from the specified files.
- [var openDocument: some AppSchemaIntent](./opendocument.md)
  An intent schema that opens the specified files in the reader.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerintent/openpage)*