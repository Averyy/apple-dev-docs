# numberValue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The value of the metadata item as a number.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var numberValue: NSNumber? { get }
```

## Discussion

This value is `nil` if the system can’t represent the value as a number.

## See Also

### Accessing values
- [var value: (any NSCopying & NSObjectProtocol)?](./value.md)
  The value for the mutable metadata item.
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](./extraattributes.md)
  A dictionary of additional attributes for a metadata item.
- [var dataType: String?](./datatype.md)
  The data type of the metadata item’s value.
- [var stringValue: String?](./stringvalue.md)
  The value of the metadata item as a string.
- [var dateValue: Date?](./datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](./datavalue.md)
  The value of the metadata item as a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/numbervalue)*