# AVMutableComposition

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMutableComposition : AVComposition
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

### Creating a composition
- [convenience init(urlAssetInitializationOptions: [String : Any]?)](./avmutablecomposition/init%28urlassetinitializationoptions%29-rh4y.md)
  Creates a mutable composition that uses the specified initialization options.
### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVMutableCompositionTrack]>](./avpartialasyncproperty/tracks-92p4a.md)
  The tracks that a composition contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMutableCompositionTrack?, (any Error)?) -> Void)](./avmutablecomposition/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableCompositionTrack]?, (any Error)?) -> Void)](./avmutablecomposition/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMutableCompositionTrack]?, (any Error)?) -> Void)](./avmutablecomposition/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.
### Accessing tracks
- [var tracks: [AVMutableCompositionTrack]](./avmutablecomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](./avmutablecomposition/track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](./avmutablecomposition/tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](./avmutablecomposition/tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.
### Managing composition tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableCompositionTrack?](./avmutablecomposition/mutabletrack%28compatiblewith%29.md)
  Returns a composition track into which you can insert any time range of the specified asset track.
- [func addMutableTrack(withMediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](./avmutablecomposition/addmutabletrack%28withmediatype,preferredtrackid%29.md)
  Adds an empty track to a composition.
- [func removeTrack(AVCompositionTrack)](./avmutablecomposition/removetrack%28_%29.md)
  Removes a specified track from the composition.
### Managing Cinematic tracks
- [func addTracks(for: CNAssetInfo, preferredStartingTrackID: CMPersistentTrackID) -> CNCompositionInfo](./avmutablecomposition/addtracks%28for,preferredstartingtrackid%29.md)
### Managing time ranges
- [func removeTimeRange(CMTimeRange)](./avmutablecomposition/removetimerange%28_%29.md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./avmutablecomposition/scaletimerange%28_,toduration%29.md)
  Changes the duration of all tracks in a given time range.
- [func insertEmptyTimeRange(CMTimeRange)](./avmutablecomposition/insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](./avmutablecomposition/inserttimerange%28_,of,at,completionhandler%29.md)
  Inserts all tracks of an asset for a time range into a composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](./avmutablecomposition/inserttimerange%28_,of,at%29.md)
  Inserts all the tracks within a given time range of a specified asset into the composition.
### Configuring video size
- [var naturalSize: CGSize](./avmutablecomposition/naturalsize.md)
  The encoded or authored size of the visual portion of the asset.
### Instance methods
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, isolation: isolated (any Actor)?) async throws](./avmutablecomposition/inserttimerange%28_,of,at,isolation%29.md)
### Initializers
- [convenience init(URLAssetInitializationOptions: [String : Any]?)](./avmutablecomposition/init%28urlassetinitializationoptions%29-6codz.md)

## Relationships

### Inherits From
- [AVComposition](./avcomposition.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](./avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Mutable compositions
- [class AVMutableCompositionTrack](./avmutablecompositiontrack.md)
  A mutable track in a composition that you use to insert, remove, and scale track segments without affecting their low-level representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition)*