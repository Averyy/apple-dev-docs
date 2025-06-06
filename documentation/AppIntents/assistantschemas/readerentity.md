# AssistantSchemas.ReaderEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe documents.

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
protocol ReaderEntity : AssistantSchemas.Model
```

## Mentions

- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](assistantschemas/readerentity/document.md)
  The app entity describes a document.
- [var page: some AssistantSchemas.Entity](assistantschemas/readerentity/page.md)
  The app entity describes a page.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s document viewing and editing functionality with Siri and Apple Intelligence.
- [AssistantSchemas.ReaderIntent](assistantschemas/readerintent.md)
  Assistant schema conformance for app intents that offer document viewing and editing functionality.
- [AssistantSchemas.ReaderEnum](assistantschemas/readerenum.md)
  Assistant schema conformance for types you use to describe documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerentity)*