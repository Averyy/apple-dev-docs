# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a track that contains the specified identifier.

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
func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?
```

```objc
- (AVMutableCompositionTrack *) trackWithTrackID:(CMPersistentTrackID) trackID;
```

#### Return Value

A composition track or `nil` if no track is available.

#### Discussion

Apple discourages using this method. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](./loadtrack%28withtrackid,completionhandler%29.md) instead.

## Parameters

- `trackID`: The persistent track identifier.

## See Also

### Accessing tracks
- [var tracks: [AVMutableCompositionTrack]](./tracks.md)
  The tracks that a composition contains.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/track(withtrackid:))*