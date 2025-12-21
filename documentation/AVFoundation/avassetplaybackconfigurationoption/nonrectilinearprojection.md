# nonRectilinearProjection

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let nonRectilinearProjection: AVAssetPlaybackConfigurationOption
```

#### Discussion

Clients may use this property to determine whether to configure a non-rectilinear projection when displaying video.

## See Also

- [static let stereoVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/stereovideo.md)
  An option that indicates whether the asset can render as stereo video.
- [static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/stereomultiviewvideo.md)
  An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [static let spatialVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/spatialvideo.md)
  An option that indicates whether the asset can render as spatial video.
- [static let appleImmersiveVideo: AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption/appleimmersivevideo.md)
  Indicates whether the asset is Apple Immersive Video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/nonrectilinearprojection)*