# loadTracks(withMediaCharacteristic:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic, completionHandler: @escaping @Sendable ([AVAssetTrack]?, (any Error)?) -> Void)
```

```swift
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) async throws -> [AVAssetTrack]
```

```objc
- (void) loadTracksWithMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic completionHandler:(void (^)(NSArray<AVAssetTrack *> *, NSError *)) completionHandler;
```

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

  - **tracks**: An array of tracks, which may be empty if no tracks with the specified media characteristic exist. The value is `nil` if an error occurs.
  - **error**: An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVAssetTrack]>](../avpartialasyncproperty/tracks-48zyw.md)
  The tracks of media that an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVAssetTrack?, (any Error)?) -> Void)](./loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](./loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func findUnusedTrackID(completionHandler: (CMPersistentTrackID, (any Error)?) -> Void)](./findunusedtrackid%28completionhandler%29.md)
  Loads an identifier that no other track in the asset uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/loadtracks(withmediacharacteristic:completionhandler:))*