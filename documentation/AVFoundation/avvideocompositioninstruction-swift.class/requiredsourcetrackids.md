# requiredSourceTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifiers of source video tracks that the compositor requires to compose frames for the instruction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requiredSourceTrackIDs: [NSValue] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSValue *> * requiredSourceTrackIDs;
```

## See Also

### Identifying source tracks
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](./requiredsourcesampledatatrackids.md)
  The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [var passthroughTrackID: CMPersistentTrackID](./passthroughtrackid.md)
  The track identifier from an instruction source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcetrackids)*