# dateValue

**Framework**: AVFoundation  
**Kind**: property

The value of the metadata item as a date.

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
var dateValue: Date? { get }
```

#### Discussion

This value is `nil` if the system can’t represent the value as a date.

## See Also

- [var value: (any NSCopying & NSObjectProtocol)?](avmetadataitem/value.md)
  The value of the metadata item.
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](avmetadataitem/extraattributes.md)
  A dictionary of additional attributes for a metadata item.
- [var stringValue: String?](avmetadataitem/stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](avmetadataitem/numbervalue.md)
  The value of the metadata item as a number.
- [var dataValue: Data?](avmetadataitem/datavalue.md)
  The value of the metadata item as a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/datevalue)*