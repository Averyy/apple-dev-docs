# AssistantSchemas.ReaderIntent

**Framework**: App Intents  
**Kind**: protocol

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

## Mentions

- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var deletePages: some AssistantSchemas.Intent](assistantschemas/readerintent/deletepages.md)
  The app intent conforms to the schema for deleting a page.
- [var enhanceDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/enhancedocuments.md)
  The app intent conforms to the schema for enhancing a document.
- [var insertPages: some AssistantSchemas.Intent](assistantschemas/readerintent/insertpages.md)
  The app intent conforms to the schema for inserting a page.
- [var openDocument: some AssistantSchemas.Intent](assistantschemas/readerintent/opendocument.md)
  The app intent conforms to the schema for opening a text document.
- [var openPage: some AssistantSchemas.Intent](assistantschemas/readerintent/openpage.md)
  The app intent conforms to the schema for opening a document.
- [var resizeDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/resizedocuments.md)
  The app intent conforms to the schema for resizing a document.
- [var rotateDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/rotatedocuments.md)
  The app intent conforms to the schema for rotating a document.
- [var rotatePages: some AssistantSchemas.Intent](assistantschemas/readerintent/rotatepages.md)
  The app intent conforms to the schema for rotating a page.
- [var searchDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/searchdocuments.md)
  The app intent conforms to the schema for searching in a document.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s document viewing and editing functionality with Siri and Apple Intelligence.
- [AssistantSchemas.ReaderEntity](assistantschemas/readerentity.md)
  Assistant schema conformance for app entities that describe documents.
- [AssistantSchemas.ReaderEnum](assistantschemas/readerenum.md)
  Assistant schema conformance for types you use to describe documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerintent)*