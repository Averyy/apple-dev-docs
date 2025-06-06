# AVAssetPlaybackConfigurationOption

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines playback configuration options for an asset.

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
struct AVAssetPlaybackConfigurationOption
```

## Topics

### Configuration Options
- [static let stereoVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/stereovideo.md)
  An option that indicates whether the asset can render as stereo video.
- [static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/stereomultiviewvideo.md)
  An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [static let spatialVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/spatialvideo.md)
  An option that indicates whether the asset can render as spatial video.
### Initializers
- [init(rawValue: String)](avassetplaybackconfigurationoption/init(rawvalue:).md)
  Creates a configuration option from its raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVAssetPlaybackAssistant](avassetplaybackassistant.md)
  An object that provides playback information for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption)*