# AssistantSchemas.PresentationEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app entities that describe presentation data.

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
protocol PresentationEntity : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](./presentationentity/document.md)
  The app entity describes a presentation.
- [var slide: some AssistantSchemas.Entity](./presentationentity/slide.md)
  The app entity describes a slide.
- [var template: some AssistantSchemas.Entity](./presentationentity/template.md)
  The app entity describes a template for a presentation.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationentity)*