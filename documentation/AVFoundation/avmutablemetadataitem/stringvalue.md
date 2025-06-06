# stringValue

**Framework**: AVFoundation  
**Kind**: property

The value of the metadata item as a string.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var stringValue: String? { get }
```

#### Discussion

This value is `nil` if the system can’t represent the value as a string.

## See Also

- [var value: (any NSCopying & NSObjectProtocol)?](avmutablemetadataitem/value.md)
  The value for the mutable metadata item.
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](avmutablemetadataitem/extraattributes.md)
  A dictionary of additional attributes for a metadata item.
- [var dataType: String?](avmutablemetadataitem/datatype.md)
  The data type of the metadata item’s value.
- [var numberValue: NSNumber?](avmutablemetadataitem/numbervalue.md)
  The value of the metadata item as a number.
- [var dateValue: Date?](avmutablemetadataitem/datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](avmutablemetadataitem/datavalue.md)
  The value of the metadata item as a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/stringvalue)*