# AVMetadataItem

**Framework**: AVFoundation  
**Kind**: class

A metadata item for an audiovisual asset or one of its tracks.

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
class AVMetadataItem
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)
- [Retrieving media metadata](retrieving-media-metadata.md)
- [Presenting chapter markers](presenting-chapter-markers.md)

#### Overview

To effectively use `AVMetadataItem`, you need to understand how [`AVFoundation`](AVFoundation.md) organizes metadata. To simplify finding and filtering metadata items, the framework groups related metadata into key spaces:

-  The framework defines several format-specific key spaces. They roughly correlate to a particular container or file format, such as QuickTime (QuickTime metadata and user data) or MP3 (ID3). However, a single asset may contain metadata values across multiple key spaces. To retrieve an asset’s complete collection of format-specific metadata, you use its [`metadata`](avasset/metadata.md) property.
-  There are several common metadata values, such as a movie’s creation date or description, that can exist across multiple key spaces. To help normalize access to this common metadata, the framework provides a common key space that gives access to a limited set of metadata values common to several key spaces. This makes it easy to retrieve commonly used metadata without concern for the specific format. To retrieve an asset’s collection of common metadata, you use its [`commonMetadata`](avasset/commonmetadata.md) property.

Metadata items have keys that accord with the specification of the container format from which they’re drawn. Full details of the metadata formats, metadata keys, and metadata key spaces supported by AVFoundation are available in [`AVMetadataKeySpace`](avmetadatakeyspace.md) and [`AVMetadataKey`](avmetadatakey.md).

To load values of a metadata item when you access them for the first time, use the methods from the [`AVAsynchronousKeyValueLoading`](avasynchronouskeyvalueloading.md) protocol. The [`AVAsset`](avasset.md) class and other classes in turn provide their metadata as needed so that you can obtain objects from those arrays without incurring overhead for items you don’t inspect.

To filter arrays of metadata items, you use the methods of this class. For example, you can filter by key and key space, by locale, and by preferred language.

## Topics

### Creating a metadata item
- [init(propertiesOfMetadataItem: AVMetadataItem, valueLoadingHandler: (AVMetadataItemValueRequest) -> Void)](avmetadataitem/init(propertiesofmetadataitem:valueloadinghandler:).md)
  Creates a metadata item whose value loads on an on-demand basis only.
- [class AVMetadataItemValueRequest](avmetadataitemvaluerequest.md)
  An object that responds to a request to load the value of a metadata item.
### Identifying metadata items
- [var identifier: AVMetadataIdentifier?](avmetadataitem/identifier.md)
  An identifier for a metadata item.
### Loading values
- [var dataType: String?](avmetadataitem/datatype.md)
  The data type of the metadata item’s value.
- [static var value: AVAsyncProperty<Root, (any NSCopying & NSObjectProtocol)?>](avpartialasyncproperty/value.md)
  The value of the metadata item.
- [static var stringValue: AVAsyncProperty<Root, String?>](avpartialasyncproperty/stringvalue.md)
  The value of the metadata item as a string.
- [static var numberValue: AVAsyncProperty<Root, NSNumber?>](avpartialasyncproperty/numbervalue.md)
  The value of the metadata item as a number.
- [static var dateValue: AVAsyncProperty<Root, Date?>](avpartialasyncproperty/datevalue.md)
  The value of the metadata item as a date.
- [static var dataValue: AVAsyncProperty<Root, Data?>](avpartialasyncproperty/datavalue.md)
  The value of the metadata item as a data value.
- [static var extraAttributes: AVAsyncProperty<Root, [AVMetadataExtraAttributeKey : Any]?>](avpartialasyncproperty/extraattributes.md)
  A dictionary of additional attributes for the item.
### Accessing keys and key spaces
- [var key: (any NSCopying & NSObjectProtocol)?](avmetadataitem/key.md)
  The key of the metadata item.
- [var commonKey: AVMetadataKey?](avmetadataitem/commonkey.md)
  The common key of the metadata item.
- [var keySpace: AVMetadataKeySpace?](avmetadataitem/keyspace.md)
  The key space for the metadata item’s key.
### Accessing timing
- [var time: CMTime](avmetadataitem/time.md)
  The timestamp of the metadata item.
- [var startDate: Date?](avmetadataitem/startdate.md)
  The start date of the timed metadata.
- [var duration: CMTime](avmetadataitem/duration.md)
  The duration of the metadata item.
### Accessing language support
- [var locale: Locale?](avmetadataitem/locale.md)
  The locale of the metadata item.
- [var extendedLanguageTag: String?](avmetadataitem/extendedlanguagetag.md)
  The IETF BCP 47 (RFC 4646) language identifier of the metadata item.
### Filtering arrays of metadata items
- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredbyidentifier:).md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:withkey:keyspace:).md)
  Returns metadata items that match a specified key or key space.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:with:).md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns metadata items whose locales match one of the specified language identifiers.
- [class func metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredby:).md)
  Returns filtered metadata items.
### Translating metadata items
- [class func identifier(forKey: Any, keySpace: AVMetadataKeySpace) -> AVMetadataIdentifier?](avmetadataitem/identifier(forkey:keyspace:).md)
  Returns a metadata identifier for the specified key and key space.
- [class func key(forIdentifier: AVMetadataIdentifier) -> Any?](avmetadataitem/key(foridentifier:).md)
  Returns a metadata key for the specified identifier.
- [class func keySpace(forIdentifier: AVMetadataIdentifier) -> AVMetadataKeySpace?](avmetadataitem/keyspace(foridentifier:).md)
  Returns a metadata key space for the specified identifier.
### Accessing values
- [var value: (any NSCopying & NSObjectProtocol)?](avmetadataitem/value.md)
  The value of the metadata item.
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](avmetadataitem/extraattributes.md)
  A dictionary of additional attributes for a metadata item.
- [var stringValue: String?](avmetadataitem/stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](avmetadataitem/numbervalue.md)
  The value of the metadata item as a number.
- [var dateValue: Date?](avmetadataitem/datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](avmetadataitem/datavalue.md)
  The value of the metadata item as a data value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMutableMetadataItem](avmutablemetadataitem.md)
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

- [Retrieving media metadata](retrieving-media-metadata.md)
  Load descriptive metadata for media assets and their tracks.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem)*