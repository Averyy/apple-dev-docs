# AVPartialAsyncProperty

**Framework**: AVFoundation  
**Kind**: class

An asynchronous property that constrains its type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AVPartialAsyncProperty<Root>
```

#### Overview

This class defines the [`AVAsyncProperty`](avasyncproperty.md) constants for various AVFoundation types, including [`AVAsset`](avasset.md), [`AVAssetTrack`](avassettrack.md), and [`AVMetadataItem`](avmetadataitem.md).

## Topics

### Loading properties
- [AVAsset](avasset-async-properties.md)
  Asynchronous properties for assets.
- [AVAssetTrack](avassettrack-async-properties.md)
  Asynchronous properties for asset tracks.
- [AVURLAsset](avurlasset-async-properties.md)
  Asynchronous properties for URL assets.
- [AVFragmentedAsset](avfragmentedasset-async-properties.md)
  Asynchronous properties for fragmented assets.
- [AVMetadataItem](avmetadataitem-async-properties.md)
  Asynchronous properties for metadata items.
- [AVComposition](avcomposition-async-properties.md)
  Asynchronous properties for compositions.
- [AVMutableComposition](avmutablecomposition-async-properties.md)
  Asynchronous properties for mutable compositions.
- [AVMovie](avmovie-async-properties.md)
  Asynchronous properties for movies.
- [AVMutableMovie](avmutablemovie-async-properties.md)
  Asynchronous properties for mutable movies.
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md)
  Asynchronous properties for fragmented movies.
### Describing a property
- [var description: String](avpartialasyncproperty/description.md)
  A description of the object.
- [static var sidecarURL: AVAsyncProperty<Root, URL?>](avpartialasyncproperty/sidecarurl.md)
  The sidecar URL used by the MediaExtension. The sidecar URL is returned only if the MediaExtension format reader supports sidecar files, and implements this property [MEFileInfo setSidecarFilename:]. Will return nil otherwise.

## Relationships

### Inherits From
- [AVAnyAsyncProperty](avanyasyncproperty.md)
### Inherited By
- [AVAsyncProperty](avasyncproperty.md)
### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
  A protocol that defines the interface to load media data asynchronously.
- [class AVAsyncProperty](avasyncproperty.md)
  An asynchronous property that constrains its type and value.
- [class AVAnyAsyncProperty](avanyasyncproperty.md)
  A base class for asynchronous properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty)*