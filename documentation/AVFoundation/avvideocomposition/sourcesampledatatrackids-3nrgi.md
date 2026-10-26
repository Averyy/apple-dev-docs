# sourceSampleDataTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifiers of source sample data tracks in the composition that the compositor requires to compose frames.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * sourceSampleDataTrackIDs;
```

## See Also

### Identifying source tracks
- [var sourceTrackIDForFrameTiming: CMPersistentTrackID](./sourcetrackidforframetiming.md)
  An identifier of the source track from which the video composition derives frame timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/sourcesampledatatrackids-3nrgi)*