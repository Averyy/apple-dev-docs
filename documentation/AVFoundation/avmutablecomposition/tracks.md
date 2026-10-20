# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The tracks that a composition contains.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var tracks: [AVMutableCompositionTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMutableCompositionTrack *> * tracks;
```

#### Discussion

In a mutable composition, the tracks are instances of [`AVMutableCompositionTrack`](../avmutablecompositiontrack.md), whereas in [`AVComposition`](../avcomposition.md) the tracks are instances of [`AVCompositionTrack`](../avcompositiontrack.md).

## See Also

### Accessing tracks
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks)*