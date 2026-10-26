# dateValue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The value of the metadata item as a date.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`dateValue`](../avpartialasyncproperty/datevalue.md) asynchronously instead.

## Declaration

```swift
var dateValue: Date? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDate * dateValue;
```

#### Discussion

This value is `nil` if the system can’t represent the value as a date.

## See Also

### Accessing values
- [var value: (any NSCopying & NSObjectProtocol)?](./value.md)
  The value of the metadata item.
- [var extraAttributes: [AVMetadataExtraAttributeKey : Any]?](./extraattributes.md)
  A dictionary of additional attributes for a metadata item.
- [var stringValue: String?](./stringvalue.md)
  The value of the metadata item as a string.
- [var numberValue: NSNumber?](./numbervalue.md)
  The value of the metadata item as a number.
- [var dataValue: Data?](./datavalue.md)
  The value of the metadata item as a data value.
- [- loadValuesAsynchronouslyForKeys:completionHandler:](./loadvaluesasynchronouslyforkeys_completionhandler_.md)
  Tells the object to load the values of any of the specified keys that aren’t already loaded.
- [- statusOfValueForKey:error:](./statusofvalueforkey_error_.md)
  Reports whether the value for a given key is immediately available without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/datevalue)*