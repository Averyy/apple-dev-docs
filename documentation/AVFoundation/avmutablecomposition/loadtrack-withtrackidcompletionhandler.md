# loadTrack(withTrackID:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads a track that contains the specified identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID) async throws -> AVMutableCompositionTrack?
```

## Parameters

- `trackID`: The identifier of the track to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var tracks: AVAsyncProperty<Root, [AVMutableCompositionTrack]>](avpartialasyncproperty/tracks-92p4a.md)
  The tracks that a composition contains.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableCompositionTrack]?, (any Error)?) -> Void)](avmutablecomposition/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMutableCompositionTrack]?, (any Error)?) -> Void)](avmutablecomposition/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/loadtrack(withtrackid:completionhandler:))*