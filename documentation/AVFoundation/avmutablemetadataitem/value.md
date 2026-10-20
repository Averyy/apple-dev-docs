# value

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readwrite, nullable) id<NSCopying,NSObject> value;
```

## See Also

### Accessing values
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](./extraattributes.md)
  A dictionary of additional attributes for a metadata item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/value)*