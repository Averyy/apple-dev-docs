# loadTrack(withTrackID:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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
func loadTrack(withTrackID trackID: CMPersistentTrackID, completionHandler: @escaping @Sendable (AVFragmentedAssetTrack?, (any Error)?) -> Void)
```

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID) async throws -> AVFragmentedAssetTrack?
```

```objc
- (void) loadTrackWithTrackID:(CMPersistentTrackID) trackID completionHandler:(void (^)(AVFragmentedAssetTrack *, NSError *)) completionHandler;
```

## Parameters

- `trackID`: The identifier of the track to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

  - **track**: The loaded track, or `nil` if no track with the specified identifier exists or if an error occurs.
  - **error**: An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVFragmentedAssetTrack]>](../avpartialasyncproperty/tracks-9z3j9.md)
  The tracks an asset contains.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](./loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](./loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/loadtrack(withtrackid:completionhandler:))*