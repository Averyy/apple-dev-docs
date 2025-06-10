# AssistantSchemas.PresentationEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe presentation data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol PresentationEntity : AssistantSchemas.Model
```

## Mentions

- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](assistantschemas/presentationentity/document.md)
  The app entity describes a presentation.
- [var slide: some AssistantSchemas.Entity](assistantschemas/presentationentity/slide.md)
  The app entity describes a slide.
- [var template: some AssistantSchemas.Entity](assistantschemas/presentationentity/template.md)
  The app entity describes a template for a presentation.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s presentation functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PresentationIntent](assistantschemas/presentationintent.md)
  Assistant schema conformance for app intents that offer presentation functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationentity)*