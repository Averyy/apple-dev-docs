# dataValue

**Framework**: AVFoundation  
**Kind**: property

The value of the metadata item as a data value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var dataValue: AVAsyncProperty<Root, Data?> { get }
```

## Mentions

- [Retrieving media metadata](retrieving-media-metadata.md)

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

## See Also

- [var dataType: String?](avmetadataitem/datatype.md)
  The data type of the metadata item’s value.
- [static var value: AVAsyncProperty<Root, (any NSCopying & NSObjectProtocol)?>](avpartialasyncproperty/value.md)
  The value of the metadata item.
- [static var stringValue: AVAsyncProperty<Root, String?>](avpartialasyncproperty/stringvalue.md)
  The value of the metadata item as a string.
- [static var numberValue: AVAsyncProperty<Root, NSNumber?>](avpartialasyncproperty/numbervalue.md)
  The value of the metadata item as a number.
- [static var dateValue: AVAsyncProperty<Root, Date?>](avpartialasyncproperty/datevalue.md)
  The value of the metadata item as a date.
- [static var extraAttributes: AVAsyncProperty<Root, [AVMetadataExtraAttributeKey : Any]?>](avpartialasyncproperty/extraattributes.md)
  A dictionary of additional attributes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/datavalue)*