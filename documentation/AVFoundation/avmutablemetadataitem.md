# AVMutableMetadataItem

**Framework**: AVFoundation  
**Kind**: class

A mutable metadata item for an audiovisual asset or for one of its tracks.

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
class AVMutableMetadataItem
```

#### Overview

You can initialize a mutable metadata item from an existing [`AVMetadataItem`](avmetadataitem.md) object or with a one or more of the basic properties of a metadata item: a key, a key space, a locale, and a value.

## Topics

### Identifying Metadata Items
- [var identifier: AVMetadataIdentifier?](avmutablemetadataitem/identifier.md)
  Indicates the identifier of the metadata item.
### Accessing Keys and Key Spaces
- [var key: (any NSCopying & NSObjectProtocol)?](avmutablemetadataitem/key.md)
  The key for a mutable metadata item.
- [var keySpace: AVMetadataKeySpace?](avmutablemetadataitem/keyspace.md)
  The key space of the metadata item’s key.
### Accessing Values
- [var value: (any NSCopying & NSObjectProtocol)?](avmutablemetadataitem/value.md)
  The value for the mutable metadata item.
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](avmutablemetadataitem/extraattributes.md)
  A dictionary of additional attributes for a metadata item.
- [var dataType: String?](avmutablemetadataitem/datatype.md)
  The data type of the metadata item’s value.
- [var stringValue: String?](avmutablemetadataitem/stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](avmutablemetadataitem/numbervalue.md)
  The value of the metadata item as a number.
- [var dateValue: Date?](avmutablemetadataitem/datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](avmutablemetadataitem/datavalue.md)
  The value of the metadata item as a data value.
### Accessing Timing
- [var time: CMTime](avmutablemetadataitem/time.md)
  The timestamp for a mutable metadata item.
- [var startDate: Date?](avmutablemetadataitem/startdate.md)
  The start date of the timed metadata.
- [var duration: CMTime](avmutablemetadataitem/duration.md)
  The duration of a mutable metadata item.
### Accessing Language Support
- [var locale: Locale?](avmutablemetadataitem/locale.md)
  The locale for a mutable metadata item.
- [var extendedLanguageTag: String?](avmutablemetadataitem/extendedlanguagetag.md)
  The IETF BCP 47 (RFC 4646) language identifier of the metadata item.

## Relationships

### Inherits From
- [AVMetadataItem](avmetadataitem.md)
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
- [class AVMetadataItem](avmetadataitem.md)
  A metadata item for an audiovisual asset or one of its tracks.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem)*