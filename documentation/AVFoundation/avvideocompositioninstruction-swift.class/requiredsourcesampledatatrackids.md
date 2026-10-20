# requiredSourceSampleDataTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var requiredSourceSampleDataTrackIDs: [NSNumber] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * requiredSourceSampleDataTrackIDs;
```

## See Also

### Identifying source tracks
- [var requiredSourceTrackIDs: [NSValue]](./requiredsourcetrackids.md)
  The identifiers of source video tracks that the compositor requires to compose frames for the instruction.
- [var passthroughTrackID: CMPersistentTrackID](./passthroughtrackid.md)
  The track identifier from an instruction source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids)*