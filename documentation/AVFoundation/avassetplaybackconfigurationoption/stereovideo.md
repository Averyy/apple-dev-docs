# stereoVideo

**Framework**: AVFoundation  
**Kind**: property

An option that indicates whether the asset can render as stereo video.

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
static let stereoVideo: AVAssetPlaybackConfigurationOption
```

#### Discussion

Apps may use this property to determine whether to configure stereo video rendering.

## See Also

- [static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/stereomultiviewvideo.md)
  An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [static let spatialVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/spatialvideo.md)
  An option that indicates whether the asset can render as spatial video.
- [static let appleImmersiveVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/appleimmersivevideo.md)
  Indicates whether the asset is Apple Immersive Video.
- [static let nonRectilinearProjection: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/nonrectilinearprojection.md)
  Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/stereovideo)*