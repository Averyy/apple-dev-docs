# unusedTrackID()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an identifier that no other tracks in the asset use.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func unusedTrackID() -> CMPersistentTrackID
```

```objc
- (CMPersistentTrackID) unusedTrackID;
```

#### Return Value

An unused [`CMPersistentTrackID`](../../CoreMedia/cmpersistenttrackid.md) value.

## See Also

### Accessing tracks
- [var tracks: [AVCompositionTrack]](./tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/unusedtrackid())*