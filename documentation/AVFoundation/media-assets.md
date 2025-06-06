# Media assets

**Framework**: AVFoundation

Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.

## Topics

### Essentials
- [Loading media data asynchronously](loading-media-data-asynchronously.md)
  Build responsive apps by using language-level concurrency features to efficiently load media data.
### Assets
- [class AVAsset](avasset.md)
  An object that models timed audiovisual media.
- [class AVURLAsset](avurlasset.md)
  An asset that represents media at a local or remote URL.
- [class AVAssetTrack](avassettrack.md)
  An object that models a track of media that an asset contains.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.
- [class AVAssetTrackGroup](avassettrackgroup.md)
  A group of related tracks in an asset.
### Metadata
- [Retrieving media metadata](retrieving-media-metadata.md)
  Load descriptive metadata for media assets and their tracks.
- [class AVMetadataItem](avmetadataitem.md)
  A metadata item for an audiovisual asset or one of its tracks.
- [class AVMutableMetadataItem](avmutablemetadataitem.md)
  A mutable metadata item for an audiovisual asset or for one of its tracks.
- [struct AVMetadataIdentifier](avmetadataidentifier.md)
  A structure that defines identifiers for metadata formats.
- [struct AVMetadataKey](avmetadatakey.md)
  A structure that defines a metadata key.
- [struct AVMetadataKeySpace](avmetadatakeyspace.md)
  A structure that defines a metadata key space.
- [struct AVMetadataExtraAttributeKey](avmetadataextraattributekey.md)
  A structure that defines keys for extra metadata attributes.
- [struct AVMetadataFormat](avmetadataformat.md)
  A structure that defines metadata formats.
- [class AVMetadataItemFilter](avmetadataitemfilter.md)
  An object that filters selected information from a metadata item.
### Property loading
- [protocol AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
  A protocol that defines the interface to load media data asynchronously.
- [class AVAsyncProperty](avasyncproperty.md)
  An asynchronous property that constrains its type and value.
- [class AVPartialAsyncProperty](avpartialasyncproperty.md)
  An asynchronous property that constrains its type.
- [class AVAnyAsyncProperty](avanyasyncproperty.md)
  A base class for asynchronous properties.
### Fragmented assets
- [class AVFragmentedAsset](avfragmentedasset.md)
  An asset with a duration that the system can extend without modifying its existing media data.
- [class AVFragmentedAssetTrack](avfragmentedassettrack.md)
  An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [class AVFragmentedAssetMinder](avfragmentedassetminder.md)
  An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.

## See Also

- [Media reading and writing](media-reading-and-writing.md)
  Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- [Media types and utilities](media-types-and-utilities.md)
  Identify the types of content and file formats that AVFoundation supports.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/media-assets)*