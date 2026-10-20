# AssistantSchemas.ReaderIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app intents that offer document viewing and editing functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol ReaderIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var deletePages: some AssistantSchemas.Intent](./readerintent/deletepages.md)
  The app intent conforms to the schema for deleting a page.
- [var enhanceDocuments: some AssistantSchemas.Intent](./readerintent/enhancedocuments.md)
  The app intent conforms to the schema for enhancing a document.
- [var insertPages: some AssistantSchemas.Intent](./readerintent/insertpages.md)
  The app intent conforms to the schema for inserting a page.
- [var openDocument: some AssistantSchemas.Intent](./readerintent/opendocument.md)
  The app intent conforms to the schema for opening a text document.
- [var openPage: some AssistantSchemas.Intent](./readerintent/openpage.md)
  The app intent conforms to the schema for opening a document.
- [var resizeDocuments: some AssistantSchemas.Intent](./readerintent/resizedocuments.md)
  The app intent conforms to the schema for resizing a document.
- [var rotateDocuments: some AssistantSchemas.Intent](./readerintent/rotatedocuments.md)
  The app intent conforms to the schema for rotating a document.
- [var rotatePages: some AssistantSchemas.Intent](./readerintent/rotatepages.md)
  The app intent conforms to the schema for rotating a page.
- [var searchDocuments: some AssistantSchemas.Intent](./readerintent/searchdocuments.md)
  The app intent conforms to the schema for searching in a document.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](../assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](./intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerintent)*