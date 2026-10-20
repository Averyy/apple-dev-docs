# AVAssetPlaybackConfigurationOption

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * AVAssetPlaybackConfigurationOption;
```

## Topics

### Configuration options
- [static let stereoVideo: AVAssetPlaybackConfigurationOption](./avassetplaybackconfigurationoption/stereovideo.md)
  An option that indicates whether the asset can render as stereo video.
- [static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption](./avassetplaybackconfigurationoption/stereomultiviewvideo.md)
  An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [static let spatialVideo: AVAssetPlaybackConfigurationOption](./avassetplaybackconfigurationoption/spatialvideo.md)
  An option that indicates whether the asset can render as spatial video.
- [static let appleImmersiveVideo: AVAssetPlaybackConfigurationOption](./avassetplaybackconfigurationoption/appleimmersivevideo.md)
  Indicates whether the asset is Apple Immersive Video.
- [static let nonRectilinearProjection: AVAssetPlaybackConfigurationOption](./avassetplaybackconfigurationoption/nonrectilinearprojection.md)
  Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.
### Initializers
- [init(rawValue: String)](./avassetplaybackconfigurationoption/init%28rawvalue%29.md)
  Creates a configuration option from its raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Utilities
- [class AVAssetPlaybackAssistant](./avassetplaybackassistant.md)
  An object that provides playback information for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption)*