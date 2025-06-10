# AssistantSchemas.PhotosEnum

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for types you use to describe photos and videos.

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
protocol PhotosEnum : AssistantSchemas.Model
```

## Mentions

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var albumType: some AssistantSchemas.Enum](assistantschemas/photosenum/albumtype.md)
  The type of photo album.
- [var assetType: some AssistantSchemas.Enum](assistantschemas/photosenum/assettype.md)
  The type of asset.
- [var filterType: some AssistantSchemas.Enum](assistantschemas/photosenum/filtertype.md)
  The filter effect for a photo or video.
- [var rotationDirection: some AssistantSchemas.Enum](assistantschemas/photosenum/rotationdirection.md)
  The direction for rotating a photo or video.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EnumSchema](assistantschema/enumschema.md)
- [AssistantSchemas.EnumSchema](assistantschemas/enumschema.md)

## See Also

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s photo and video functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PhotosIntent](assistantschemas/photosintent.md)
  Assistant schema conformance for app intents that offer photo and video functionality.
- [AssistantSchemas.PhotosEntity](assistantschemas/photosentity.md)
  Assistant schema conformance for app entities that describe media assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosenum)*