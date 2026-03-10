# filterType

**Framework**: App Intents  
**Kind**: property

The filter effect for a photo or video.

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
var filterType: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.photos.filterType` schema:

```swift
@AppEnum(schema: .photos.filterType)
enum PhotoFilterEffectType: AppEnum {
    case original

    static var caseDisplayRepresentations: [PhotoFilterEffectType: AppIntents.DisplayRepresentation] = [
        .original: "Original",
    ]
}
```

For more information about the `.photos` app intent domain, see [`Making photo and video actions available to Siri and Apple Intelligence`](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var albumType: some AssistantSchemas.Enum](assistantschemas/photosenum/albumtype.md)
  The type of photo album.
- [var assetType: some AssistantSchemas.Enum](assistantschemas/photosenum/assettype.md)
  The type of asset.
- [var rotationDirection: some AssistantSchemas.Enum](assistantschemas/photosenum/rotationdirection.md)
  The direction for rotating a photo or video.
- [AssistantSchemas.PhotosEnum](assistantschemas/photosenum.md)
  Assistant schema conformance for types you use to describe photos and videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosenum/filtertype)*