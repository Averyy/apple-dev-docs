# AVFragmentedAsset

**Framework**: AVFoundation  
**Kind**: class

An asset with a duration that the system can extend without modifying its existing media data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVFragmentedAsset
```

#### Overview

By using an `mvex` box in their `moov` box, QuickTime movie files and MPEG-4 files can indicate that they accommodate additional fragments. To determine whether a fragmented asset can monitor the addition of fragments, check the value of its [`canContainFragments`](avasset/cancontainfragments.md) property.

Associate a fragmented asset with an instance of [`AVFragmentedAssetMinder`](avfragmentedassetminder.md) to know when the system appends new fragments. When it has an associated asset minder, [`AVFragmentedAssetTrack`](avfragmentedassettrack.md) posts [`AVAssetDurationDidChangeNotification`](avassetdurationdidchangenotification.md) notifications whenever it detects new fragments. It may also post [`AVAssetContainsFragmentsDidChangeNotification`](avassetcontainsfragmentsdidchangenotification.md) and [`AVAssetWasDefragmentedNotification`](avassetwasdefragmentednotification.md), as the documentation of those notifications explains.

## Topics

### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVFragmentedAssetTrack]>](avpartialasyncproperty/tracks-9z3j9.md)
  The tracks an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedAssetTrack?, (any Error)?) -> Void)](avfragmentedasset/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](avfragmentedasset/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](avfragmentedasset/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.
### Accessing Tracks
- [var tracks: [AVFragmentedAssetTrack]](avfragmentedasset/tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](avfragmentedasset/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediatype:).md)
  Returns tracks that present media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediacharacteristic:).md)
  Returns tracks that present media of a specified characteristic.

## Relationships

### Inherits From
- [AVURLAsset](avurlasset.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [AVContentKeyRecipient](avcontentkeyrecipient.md)
- [AVFragmentMinding](avfragmentminding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSItemProviderReading](../Foundation/NSItemProviderReading.md)
- [NSItemProviderWriting](../Foundation/NSItemProviderWriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVFragmentedAssetTrack](avfragmentedassettrack.md)
  An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [class AVFragmentedAssetMinder](avfragmentedassetminder.md)
  An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset)*