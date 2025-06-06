# loadTracks(withMediaCharacteristic:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads tracks that contain media of a specified characteristic.

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
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) async throws -> [AVFragmentedAssetTrack]
```

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var tracks: AVAsyncProperty<Root, [AVFragmentedAssetTrack]>](avpartialasyncproperty/tracks-9z3j9.md)
  The tracks an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedAssetTrack?, (any Error)?) -> Void)](avfragmentedasset/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](avfragmentedasset/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/loadtracks(withmediacharacteristic:completionhandler:))*