# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The tracks of media that an asset contains.

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
static var tracks: AVAsyncProperty<Root, [AVAssetTrack]> { get }
```

Available when `Root` inherits `AVAsset`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading tracks
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVAssetTrack?, (any Error)?) -> Void)](../avasset/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](../avasset/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](../avasset/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.
- [func findUnusedTrackID(completionHandler: (CMPersistentTrackID, (any Error)?) -> Void)](../avasset/findunusedtrackid%28completionhandler%29.md)
  Loads an identifier that no other track in the asset uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-48zyw)*