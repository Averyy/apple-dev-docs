# passthroughTrackID

**Framework**: AVFoundation  
**Kind**: property

The track identifier from an instruction source frame.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var passthroughTrackID: CMPersistentTrackID { get }
```

#### Discussion

If the video composition result is one of the source frames for the duration of the instruction, this property returns the corresponding track ID. The compositor won’t be run for the duration of the instruction and the proper source frame will be used instead. The value of this property is computed from the layer instructions

## See Also

- [var requiredSourceTrackIDs: [NSValue]](avvideocompositioninstruction-swift.class/requiredsourcetrackids.md)
  The identifiers of source video tracks that the compositor requires to compose frames for the instruction.
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids.md)
  The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/passthroughtrackid)*