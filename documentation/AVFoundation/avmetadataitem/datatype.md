# dataType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The data type of the metadata item’s value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var dataType: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * dataType;
```

## See Also

### Loading values
- [static var value: AVAsyncProperty<Root, (any NSCopying & NSObjectProtocol)?>](../avpartialasyncproperty/value.md)
  The value of the metadata item.
- [static var stringValue: AVAsyncProperty<Root, String?>](../avpartialasyncproperty/stringvalue.md)
  The value of the metadata item as a string.
- [static var numberValue: AVAsyncProperty<Root, NSNumber?>](../avpartialasyncproperty/numbervalue.md)
  The value of the metadata item as a number.
- [static var dateValue: AVAsyncProperty<Root, Date?>](../avpartialasyncproperty/datevalue.md)
  The value of the metadata item as a date.
- [static var dataValue: AVAsyncProperty<Root, Data?>](../avpartialasyncproperty/datavalue.md)
  The value of the metadata item as a data value.
- [static var extraAttributes: AVAsyncProperty<Root, [AVMetadataExtraAttributeKey : Any]?>](../avpartialasyncproperty/extraattributes.md)
  A dictionary of additional attributes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/datatype)*