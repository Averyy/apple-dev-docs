# AppSchema.PresentationEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the presentation domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol PresentationEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var document: some AppSchemaEntity](./presentationentity/document.md)
  An entity schema for a document.
- [var slide: some AppSchemaEntity](./presentationentity/slide.md)
  An entity schema for a slide.
- [var template: some AppSchemaEntity](./presentationentity/template.md)
  An entity schema for a template.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var document: some AppSchemaEntity](./presentationentity/document.md)
  An entity schema for a document.
- [var slide: some AppSchemaEntity](./presentationentity/slide.md)
  An entity schema for a slide.
- [var template: some AppSchemaEntity](./presentationentity/template.md)
  An entity schema for a template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationentity)*