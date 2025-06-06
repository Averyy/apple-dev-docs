# AssistantSchemas.PhotosEntity

**Framework**: App Intents  
**Kind**: protocol

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

## Mentions

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var album: some AssistantSchemas.Entity](assistantschemas/photosentity/album.md)
  The app entity describes an album.
- [var asset: some AssistantSchemas.Entity](assistantschemas/photosentity/asset.md)
  The app entity describes a media asset.
- [var recognizedPerson: some AssistantSchemas.Entity](assistantschemas/photosentity/recognizedperson.md)
  The app entity describes a person who appears in an asset.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s photo and video functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PhotosIntent](assistantschemas/photosintent.md)
  Assistant schema conformance for app intents that offer photo and video functionality.
- [AssistantSchemas.PhotosEnum](assistantschemas/photosenum.md)
  Assistant schema conformance for types you use to describe photos and videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosentity)*