# AssistantSchemas.PhotosEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app entities that describe media assets.

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
protocol PhotosEntity : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var album: some AssistantSchemas.Entity](./photosentity/album.md)
  The app entity describes an album.
- [var asset: some AssistantSchemas.Entity](./photosentity/asset.md)
- [var recognizedPerson: some AssistantSchemas.Entity](./photosentity/recognizedperson.md)
  The app entity describes a person who appears in an asset.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosentity)*