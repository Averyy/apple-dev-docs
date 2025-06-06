# AVMutableComposition

**Framework**: AVFoundation  
**Kind**: class

An object that you use to create a new composition from existing assets.

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
class AVMutableComposition
```

#### Overview

Use this object to add and remove composition tracks, and add, remove, and scale their time ranges. You can make an immutable snapshot of a mutable composition for playback and inspection as follows:

```swift
// Use a mutable composition object you create.
let mutableComposition = AVMutableComposition()
        
guard let composition = mutableComposition.copy() as? AVComposition else { return }
        
// Create a player item to inspect and play the composition.
let playerItem = AVPlayerItem(asset: composition)
```

## Topics

### Creating a Composition
- [convenience init(urlAssetInitializationOptions: [String : Any]?)](avmutablecomposition/init(urlassetinitializationoptions:).md)
  Creates a mutable composition that uses the specified initialization options.
### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVMutableCompositionTrack]>](avpartialasyncproperty/tracks-92p4a.md)
  The tracks that a composition contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMutableCompositionTrack?, (any Error)?) -> Void)](avmutablecomposition/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableCompositionTrack]?, (any Error)?) -> Void)](avmutablecomposition/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMutableCompositionTrack]?, (any Error)?) -> Void)](avmutablecomposition/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.
### Accessing Tracks
- [var tracks: [AVMutableCompositionTrack]](avmutablecomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](avmutablecomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](avmutablecomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](avmutablecomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.
### Managing Composition Tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableCompositionTrack?](avmutablecomposition/mutabletrack(compatiblewith:).md)
  Returns a composition track into which you can insert any time range of the specified asset track.
- [func addMutableTrack(withMediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:).md)
  Adds an empty track to a composition.
- [func removeTrack(AVCompositionTrack)](avmutablecomposition/removetrack(_:).md)
  Removes a specified track from the composition.
### Managing Cinematic Tracks
- [func addTracks(for: CNAssetInfo, preferredStartingTrackID: CMPersistentTrackID) -> CNCompositionInfo](avmutablecomposition/addtracks(for:preferredstartingtrackid:).md)
### Managing Time Ranges
- [func removeTimeRange(CMTimeRange)](avmutablecomposition/removetimerange(_:).md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablecomposition/scaletimerange(_:toduration:).md)
  Changes the duration of all tracks in a given time range.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablecomposition/insertemptytimerange(_:).md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](avmutablecomposition/inserttimerange(_:of:at:completionhandler:).md)
  Inserts all tracks of an asset for a time range into a composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](avmutablecomposition/inserttimerange(_:of:at:).md)
  Inserts all the tracks within a given time range of a specified asset into the composition.
### Configuring Video Size
- [var naturalSize: CGSize](avmutablecomposition/naturalsize.md)
  The encoded or authored size of the visual portion of the asset.
### Instance Methods
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, isolation: isolated (any Actor)?) async throws](avmutablecomposition/inserttimerange(_:of:at:isolation:).md)

## Relationships

### Inherits From
- [AVComposition](avcomposition.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMutableCompositionTrack](avmutablecompositiontrack.md)
  A mutable track in a composition that you use to insert, remove, and scale track segments without affecting their low-level representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition)*