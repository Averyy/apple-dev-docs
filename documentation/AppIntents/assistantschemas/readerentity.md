# AssistantSchemas.ReaderEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

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

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](./readerentity/document.md)
  The app entity describes a document.
- [var page: some AssistantSchemas.Entity](./readerentity/page.md)
  The app entity describes a page.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerentity)*