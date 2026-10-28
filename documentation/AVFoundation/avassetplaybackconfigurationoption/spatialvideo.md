# spatialVideo

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An option that indicates whether the asset can render as spatial video.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static let spatialVideo: AVAssetPlaybackConfigurationOption
```

```c
extern AVAssetPlaybackConfigurationOption const AVAssetPlaybackConfigurationOptionSpatialVideo;
```

## Discussion

Apps may use this property to determine whether to configure spatial video rendering.

## See Also

### Configuration options
- [static let stereoVideo: AVAssetPlaybackConfigurationOption](./stereovideo.md)
  An option that indicates whether the asset can render as stereo video.
- [static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption](./stereomultiviewvideo.md)
  An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [static let appleImmersiveVideo: AVAssetPlaybackConfigurationOption](./appleimmersivevideo.md)
  Indicates whether the asset is Apple Immersive Video.
- [static let nonRectilinearProjection: AVAssetPlaybackConfigurationOption](./nonrectilinearprojection.md)
  Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/spatialvideo)*