# AssistantSchemas.WordProcessorEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe text documents.

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
protocol WordProcessorEntity : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](assistantschemas/wordprocessorentity/document.md)
  The app entity describes a text document.
- [var page: some AssistantSchemas.Entity](assistantschemas/wordprocessorentity/page.md)
  The app entity describes a page in a text document.
- [var template: some AssistantSchemas.Entity](assistantschemas/wordprocessorentity/template.md)
  The app entity describes a text document template.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/wordprocessorentity)*