# requiredSourceSampleDataTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifiers of the sample data tracks the instruction requires to compose frames.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional var requiredSourceSampleDataTrackIDs: [NSNumber] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * requiredSourceSampleDataTrackIDs;
```

## Discussion

An empty array indicates the instruction requires no sample data.

## See Also

### Getting track ID settings
- [var passthroughTrackID: CMPersistentTrackID](./passthroughtrackid.md)
  An identifier of a source track to pass through without compositing.
- [var requiredSourceTrackIDs: [NSValue]?](./requiredsourcetrackids.md)
  The identifiers of the video tracks the instruction requires to compose frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids)*