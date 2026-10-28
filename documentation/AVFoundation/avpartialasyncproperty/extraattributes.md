# extraAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A dictionary of additional attributes for the item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var extraAttributes: AVAsyncProperty<Root, [AVMetadataExtraAttributeKey : Any]?> { get }
```

Available when `Root` inherits `AVMetadataItem`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading values
- [var dataType: String?](../avmetadataitem/datatype.md)
  The data type of the metadata item’s value.
- [static var value: AVAsyncProperty<Root, (any NSCopying & NSObjectProtocol)?>](./value.md)
  The value of the metadata item.
- [static var stringValue: AVAsyncProperty<Root, String?>](./stringvalue.md)
  The value of the metadata item as a string.
- [static var numberValue: AVAsyncProperty<Root, NSNumber?>](./numbervalue.md)
  The value of the metadata item as a number.
- [static var dateValue: AVAsyncProperty<Root, Date?>](./datevalue.md)
  The value of the metadata item as a date.
- [static var dataValue: AVAsyncProperty<Root, Data?>](./datavalue.md)
  The value of the metadata item as a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/extraattributes)*