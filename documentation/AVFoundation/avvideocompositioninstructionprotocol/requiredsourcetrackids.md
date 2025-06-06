# requiredSourceTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Required**: Yes

The identifiers of the video tracks the instruction requires to compose frames.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requiredSourceTrackIDs: [NSValue]? { get }
```

#### Discussion

If the value of this property is `nil`, the instruction requires all source tracks for composition.

## See Also

- [var passthroughTrackID: CMPersistentTrackID](avvideocompositioninstructionprotocol/passthroughtrackid.md)
  An identifier of a source track to pass through without compositing.
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids.md)
  The identifiers of the sample data tracks the instruction requires to compose frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcetrackids)*