# loadTracks(withMediaType:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Loads tracks that contain media of a specified type.

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
func loadTracks(withMediaType mediaType: AVMediaType, completionHandler: @escaping @Sendable ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)
```

```swift
func loadTracks(withMediaType mediaType: AVMediaType) async throws -> [AVFragmentedAssetTrack]
```

```objc
- (void) loadTracksWithMediaType:(AVMediaType) mediaType completionHandler:(void (^)(NSArray<AVFragmentedAssetTrack *> *, NSError *)) completionHandler;
```

## Parameters

- `mediaType`: The media type of the tracks to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading operation. It passes the completion handler the following parameters:

  - **tracks**: An array of tracks, which may be empty if no tracks with the specified media type exist. The value is `nil` if an error occurs.
  - **error**: An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVFragmentedAssetTrack]>](../avpartialasyncproperty/tracks-9z3j9.md)
  The tracks an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedAssetTrack?, (any Error)?) -> Void)](./loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](./loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/loadtracks(withmediatype:completionhandler:))*