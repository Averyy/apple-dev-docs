# appleImmersiveVideo

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Indicates whether the asset is Apple Immersive Video.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let appleImmersiveVideo: AVAssetPlaybackConfigurationOption
```

```c
extern AVAssetPlaybackConfigurationOption const AVAssetPlaybackConfigurationOptionAppleImmersiveVideo;
```

#### Discussion

Clients may use this property to switch into specific display and control modes for Apple Immersive Video playback.

## See Also

### Configuration options
- [static let stereoVideo: AVAssetPlaybackConfigurationOption](./stereovideo.md)
  An option that indicates whether the asset can render as stereo video.
- [static let stereoMultiviewVideo: AVAssetPlaybackConfigurationOption](./stereomultiviewvideo.md)
  An option that indicates whether the asset is in a multiview compression format and can render as stereo video.
- [static let spatialVideo: AVAssetPlaybackConfigurationOption](./spatialvideo.md)
  An option that indicates whether the asset can render as spatial video.
- [static let nonRectilinearProjection: AVAssetPlaybackConfigurationOption](./nonrectilinearprojection.md)
  Indicates whether the asset calls for the use of a non-rectilinear projection for rendering video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackconfigurationoption/appleimmersivevideo)*