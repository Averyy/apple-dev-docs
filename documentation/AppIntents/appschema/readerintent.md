# AppSchema.ReaderIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the reader domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol ReaderIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var deletePages: some AppSchemaIntent](appschema/readerintent/deletepages.md)
  An intent schema that deletes the specified pages.
- [var enhanceDocuments: some AppSchemaIntent](appschema/readerintent/enhancedocuments.md)
  An intent schema that enhances the documents.
- [var insertPages: some AppSchemaIntent](appschema/readerintent/insertpages.md)
  An intent schema that inserts pages from the specified files.
- [var openDocument: some AppSchemaIntent](appschema/readerintent/opendocument.md)
  An intent schema that opens the specified files in the reader.
- [var openPage: some AppSchemaIntent](appschema/readerintent/openpage.md)
  An intent schema that opens the app to the specified document page.
- [var resizeDocuments: some AppSchemaIntent](appschema/readerintent/resizedocuments.md)
  An intent schema that resizes the documents to a particular width and height.
- [var rotateDocuments: some AppSchemaIntent](appschema/readerintent/rotatedocuments.md)
  An intent schema that rotates the documents in the specified direction.
- [var rotatePages: some AppSchemaIntent](appschema/readerintent/rotatepages.md)
  An intent schema that rotates the pages in the specified direction.
- [var searchDocuments: some AppSchemaIntent](appschema/readerintent/searchdocuments.md)
  An intent schema that searches for text in the documents.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var deletePages: some AppSchemaIntent](appschema/readerintent/deletepages.md)
  An intent schema that deletes the specified pages.
- [var enhanceDocuments: some AppSchemaIntent](appschema/readerintent/enhancedocuments.md)
  An intent schema that enhances the documents.
- [var insertPages: some AppSchemaIntent](appschema/readerintent/insertpages.md)
  An intent schema that inserts pages from the specified files.
- [var openDocument: some AppSchemaIntent](appschema/readerintent/opendocument.md)
  An intent schema that opens the specified files in the reader.
- [var openPage: some AppSchemaIntent](appschema/readerintent/openpage.md)
  An intent schema that opens the app to the specified document page.
- [var resizeDocuments: some AppSchemaIntent](appschema/readerintent/resizedocuments.md)
  An intent schema that resizes the documents to a particular width and height.
- [var rotateDocuments: some AppSchemaIntent](appschema/readerintent/rotatedocuments.md)
  An intent schema that rotates the documents in the specified direction.
- [var rotatePages: some AppSchemaIntent](appschema/readerintent/rotatepages.md)
  An intent schema that rotates the pages in the specified direction.
- [var searchDocuments: some AppSchemaIntent](appschema/readerintent/searchdocuments.md)
  An intent schema that searches for text in the documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerintent)*