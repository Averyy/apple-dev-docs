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
var tracks: [AVCompositionTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCompositionTrack *> * tracks;
```

## See Also

### Accessing tracks
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/tracks)*