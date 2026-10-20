# extraAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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
var extraAttributes: [AVMetadataExtraAttributeKey : Any]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary<NSString *,id> * extraAttributes;
```

## See Also

### Accessing values
- [var value: (any NSCopying & NSObjectProtocol)?](./value.md)
  The value for the mutable metadata item.
- [var dataType: String?](./datatype.md)
  The data type of the metadata item’s value.
- [var stringValue: String?](./stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](./numbervalue.md)
  The value of the metadata item as a number.
- [var dateValue: Date?](./datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](./datavalue.md)
  The value of the metadata item as a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/extraattributes)*