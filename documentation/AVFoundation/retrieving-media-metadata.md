# Retrieving media metadata

**Framework**: AVFoundation

Load descriptive metadata for media assets and their tracks.

#### Overview

Media container formats provide metadata that describe their content. You can retrieve it to access information about the media such as the title, artwork, and creation date. AVFoundation models metadata values using the [`AVMetadataItem`](avmetadataitem.md) class. A metadata item represents a single value like a movie’s description or poster image. This class provides a simple, consistent interface to work with metadata, regardless of the underlying container and metadata formats.

##### Load an Assets Metadata

[`AVAsset`](avasset.md) provides several ways to access its metadata. You can retrieve all of its metadata by loading the value of its [`metadata`](avpartialasyncproperty/metadata-16qej.md) property. Alternatively, you can retrieve a subset of items that are common to all of the metadata formats it holds by loading the value of its [`commonMetadata`](avpartialasyncproperty/commonmetadata-3j3n4.md) property.

To retrieve format-specific collections of metadata, like [`iTunesMetadata`](avmetadataformat/itunesmetadata.md) or [`quickTimeMetadata`](avmetadataformat/quicktimemetadata.md), call an asset’s [`loadMetadata(for:completionHandler:)`](avasset/loadmetadata(for:completionhandler:).md) method, passing it a specific [`AVMetadataFormat`](avmetadataformat.md) to load. The example below iterates over the [`availableMetadataFormats`](avpartialasyncproperty/availablemetadataformats-4yiq8.md) an asset contains, and loads each format’s metadata items to process their values.

```swift
// A local or remote asset to inspect.
let asset = AVURLAsset(url: url)
for format in try await asset.load(.availableMetadataFormats) {
    let metadata = try await asset.loadMetadata(for: format)
    // Process the format-specific metadata collection.
    print("The available metadata format is \(metadata)")
}
```

##### Filter a Metadata Collection

After you load a collection of metadata, you can filter it to specific values using the class methods of [`AVMetadataItem`](avmetadataitem.md). The example below shows how to use the [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) method to find items with an identifier of [`commonIdentifierTitle`](avmetadataidentifier/commonidentifiertitle.md).

```swift
// Load the asset's metadata.
let metadata = try await asset.load(.metadata)
        
// Find the title in the common key space.
let titleItems = AVMetadataItem.metadataItems(from: metadata,
                                              filteredByIdentifier: .commonIdentifierTitle)
guard let item = titleItems.first else { return }
// Process the title item.
```

A metadata item’s filtering methods return collections of items instead of a single instance. In many cases, the returned collection contains a single element, but if the media contains localized metadata, or if you’re retrieving data from the common key space and the same value exists in multiple key spaces, the item returns a distinct value for each.

##### Find Specific Values

Retrieve the data a metadata item holds by loading its [`value`](avpartialasyncproperty/value.md) property, which is an object that adopts the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) and [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol) protocols. You can manually cast the value to an appropriate type, but it’s safer and more convenient to use the metadata item’s type conversion properties. Instead of loading the [`value`](avpartialasyncproperty/value.md) property, load its [`stringValue`](avpartialasyncproperty/stringvalue.md), [`numberValue`](avpartialasyncproperty/numbervalue.md), [`dateValue`](avpartialasyncproperty/datevalue.md), or [`dataValue`](avpartialasyncproperty/datavalue.md) properties as appropriate to convert it to a specific type. For example, the code listing below shows how to retrieve the artwork associated with an iTunes music track as a data value:

```swift
// The collection of iTunes metadata.
let iTunesMetadata = try await asset.loadMetadata(for: .iTunesMetadata)

// Filter metadata to find the asset's artwork.
guard let artworkItem = AVMetadataItem.metadataItems(from: iTunesMetadata,
                                                     filteredByIdentifier: .iTunesMetadataCoverArt).first else { return }

// Retrieve a Data object that contains the image data.
guard let imageData = try await artworkItem.load(.dataValue) else { return }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/retrieving-media-metadata)*