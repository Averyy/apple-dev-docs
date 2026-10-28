# sourceTrackIDForFrameTiming

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An identifier of the source track from which the video composition derives frame timing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var sourceTrackIDForFrameTiming: CMPersistentTrackID { get }
```

```objc
@property (nonatomic, readonly) CMPersistentTrackID sourceTrackIDForFrameTiming;
```

## Discussion

If an empty edit is encountered in the source asset’s track, the compositor composes frames as needed up to the frequency specified in [`frameDuration`](./frameduration.md) property. Otherwise the frame timing for the video composition is derived from the source asset’s track with the corresponding ID.

## See Also

### Identifying source tracks
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](./sourcesampledatatrackids-2hgue.md)
  The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [sourceSampleDataTrackIDs](./sourcesampledatatrackids-3nrgi.md)
  The identifiers of source sample data tracks in the composition that the compositor requires to compose frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/sourcetrackidforframetiming)*