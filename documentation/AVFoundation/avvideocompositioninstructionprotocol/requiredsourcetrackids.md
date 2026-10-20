# requiredSourceTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, readonly, nullable) NSArray<NSValue *> * requiredSourceTrackIDs;
```

#### Discussion

If the value of this property is `nil`, the instruction requires all source tracks for composition.

## See Also

### Getting track ID settings
- [var passthroughTrackID: CMPersistentTrackID](./passthroughtrackid.md)
  An identifier of a source track to pass through without compositing.
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](./requiredsourcesampledatatrackids.md)
  The identifiers of the sample data tracks the instruction requires to compose frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcetrackids)*