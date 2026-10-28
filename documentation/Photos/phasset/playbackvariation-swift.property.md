# playbackVariation

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The Live Photo playback variation for the asset.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var playbackVariation: PHAsset.PlaybackVariation { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetPlaybackVariation playbackVariation;
```

## Discussion

Use this value to determine whether a Live Photo plays back as a Long Exposure, Mirror (Bounce), or Autoloop (Loop):

- `PHAssetPlaybackVariationNone`: the asset is not a Live Photo, or uses the default Live Photo presentation.
- `PHAssetPlaybackVariationAutoloop`: the Live Photo plays back as a Loop.
- `PHAssetPlaybackVariationMirror`: the Live Photo plays back as a Bounce.
- `PHAssetPlaybackVariationLongExposure`: the Live Photo plays back as a Long Exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/playbackvariation-swift.property)*