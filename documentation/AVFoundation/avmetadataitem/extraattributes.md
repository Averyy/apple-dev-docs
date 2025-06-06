# extraAttributes

**Framework**: AVFoundation  
**Kind**: property

A dictionary of additional attributes for a metadata item.

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
var extraAttributes: [AVMetadataExtraAttributeKey : Any]? { get }
```

#### Discussion

Extra attributes, when they’re present, are specific to metadata container formats and keys in their associated key-spaces. For example, a metadata item can represent the “attached picture” frame defined by the ID3 tag specification with keyspace [`id3`](avmetadatakeyspace/id3.md) and key [`id3MetadataKeyAttachedPicture`](avmetadatakey/id3metadatakeyattachedpicture.md), a value that carries the image data, and extra attributes that include a description of the picture as carried in the ‘APIC’ frame of the ID3 tag.

## See Also

- [var value: (any NSCopying & NSObjectProtocol)?](avmetadataitem/value.md)
  The value of the metadata item.
- [var stringValue: String?](avmetadataitem/stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](avmetadataitem/numbervalue.md)
  The value of the metadata item as a number.
- [var dateValue: Date?](avmetadataitem/datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](avmetadataitem/datavalue.md)
  The value of the metadata item as a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/extraattributes)*