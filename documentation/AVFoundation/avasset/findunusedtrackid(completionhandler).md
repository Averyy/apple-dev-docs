# findUnusedTrackID(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Loads an identifier that no other track in the asset uses.

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
func findUnusedTrackID(completionHandler: @escaping @Sendable (CMPersistentTrackID, (any Error)?) -> Void)
```

```swift
func findUnusedTrackID() async throws -> CMPersistentTrackID
```

```objc
- (void) findUnusedTrackIDWithCompletionHandler:(void (^)(CMPersistentTrackID , NSError *)) completionHandler;
```

## Parameters

- `completionHandler`: A completion handler the system calls after it finishes the request.

## See Also

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVAssetTrack]>](../avpartialasyncproperty/tracks-48zyw.md)
  The tracks of media that an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVAssetTrack?, (any Error)?) -> Void)](./loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](./loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](./loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/findunusedtrackid(completionhandler:))*