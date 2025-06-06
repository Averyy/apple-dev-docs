# value

**Framework**: AVFoundation  
**Kind**: property

The value for the mutable metadata item.

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
@NSCopying
var value: (any NSCopying & NSObjectProtocol)? { get set }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/value)*