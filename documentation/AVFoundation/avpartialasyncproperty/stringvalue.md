# stringValue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The value of the metadata item as a string.

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
static var stringValue: AVAsyncProperty<Root, String?> { get }
```

Available when `Root` inherits `AVMetadataItem`.

## Mentions

- [Retrieving media metadata](../retrieving-media-metadata.md)

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

This value is `nil` if the system can’t represent the value as a string.

## See Also

### Loading values
- [var dataType: String?](../avmetadataitem/datatype.md)
  The data type of the metadata item’s value.
- [static var value: AVAsyncProperty<Root, (any NSCopying & NSObjectProtocol)?>](./value.md)
  The value of the metadata item.
- [static var numberValue: AVAsyncProperty<Root, NSNumber?>](./numbervalue.md)
  The value of the metadata item as a number.
- [static var dateValue: AVAsyncProperty<Root, Date?>](./datevalue.md)
  The value of the metadata item as a date.
- [static var dataValue: AVAsyncProperty<Root, Data?>](./datavalue.md)
  The value of the metadata item as a data value.
- [static var extraAttributes: AVAsyncProperty<Root, [AVMetadataExtraAttributeKey : Any]?>](./extraattributes.md)
  A dictionary of additional attributes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/stringvalue)*