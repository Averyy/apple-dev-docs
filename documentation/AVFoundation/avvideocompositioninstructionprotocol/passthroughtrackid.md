# passthroughTrackID

**Framework**: AVFoundation  
**Kind**: property  
**Required**: Yes

An identifier of a source track to pass through without compositing.

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

If an instruction indicates to pass through a source frame without compositing, this property returns the corresponding track identifier. The compositor isn’t run for the duration of the instruction, and instead passes the source frame through to the output. The system automatically matches the required dimensions, clean aperture, and pixel aspect ratio values of the source buffer.

## See Also

- [var requiredSourceTrackIDs: [NSValue]?](avvideocompositioninstructionprotocol/requiredsourcetrackids.md)
  The identifiers of the video tracks the instruction requires to compose frames.
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids.md)
  The identifiers of the sample data tracks the instruction requires to compose frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/passthroughtrackid)*