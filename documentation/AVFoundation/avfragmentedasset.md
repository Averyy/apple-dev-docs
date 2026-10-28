# AVFragmentedAsset

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVFragmentedAsset : AVURLAsset
```

## Overview

By using an `mvex` box in their `moov` box, QuickTime movie files and MPEG-4 files can indicate that they accommodate additional fragments. To determine whether a fragmented asset can monitor the addition of fragments, check the value of its [`canContainFragments`](./avasset/cancontainfragments.md) property.

Associate a fragmented asset with an instance of [`AVFragmentedAssetMinder`](./avfragmentedassetminder.md) to know when the system appends new fragments. When it has an associated asset minder, [`AVFragmentedAssetTrack`](./avfragmentedassettrack.md) posts [`AVAssetDurationDidChangeNotification`](./avassetdurationdidchangenotification.md) notifications whenever it detects new fragments. It may also post [`AVAssetContainsFragmentsDidChangeNotification`](./avassetcontainsfragmentsdidchangenotification.md) and [`AVAssetWasDefragmentedNotification`](./avassetwasdefragmentednotification.md), as the documentation of those notifications explains.

## Topics

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVFragmentedAssetTrack]>](./avpartialasyncproperty/tracks-9z3j9.md)
  The tracks an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedAssetTrack?, (any Error)?) -> Void)](./avfragmentedasset/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](./avfragmentedasset/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedAssetTrack]?, (any Error)?) -> Void)](./avfragmentedasset/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.
### Accessing tracks
- [var tracks: [AVFragmentedAssetTrack]](./avfragmentedasset/tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](./avfragmentedasset/track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](./avfragmentedasset/tracks%28withmediatype%29.md)
  Returns tracks that present media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](./avfragmentedasset/tracks%28withmediacharacteristic%29.md)
  Returns tracks that present media of a specified characteristic.
### Initializers
- [convenience init(URL: URL, options: [String : Any]?)](./avfragmentedasset/init%28url,options%29.md)
### Creating a fragmented asset
- [+ fragmentedAssetWithURL:options:](./avfragmentedasset/fragmentedassetwithurl_options_.md)
  Creates a fragmented asset for the media at the specified URL.

## Relationships

### Inherits From
- [AVURLAsset](./avurlasset.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](./avasynchronouskeyvalueloading.md)
- [AVContentKeyRecipient](./avcontentkeyrecipient.md)
- [AVFragmentMinding](./avfragmentminding.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSItemProviderReading](../Foundation/nsitemproviderreading.md)
- [NSItemProviderWriting](../Foundation/nsitemproviderwriting.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Fragmented assets
- [class AVFragmentedAssetTrack](./avfragmentedassettrack.md)
  An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [class AVFragmentedAssetMinder](./avfragmentedassetminder.md)
  An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [protocol AVFragmentMinding](./avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset)*