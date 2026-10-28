# loadValuesAsynchronouslyForKeys:completionHandler:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the object to load the values of any of the specified keys that aren’t already loaded.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
- (void) loadValuesAsynchronouslyForKeys:(NSArray<NSString *> *) keys completionHandler:(void (^)()) handler;
```

## Discussion

For full discussion, see [`AVAsynchronousKeyValueLoading`](../avasynchronouskeyvalueloading.md).

## Parameters

- `keys`: An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which represents one of the required keys.
- `handler`: The block to invoke when loading succeeds, fails, or is canceled.

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
- [var dateValue: Date?](./datevalue.md)
  The value of the metadata item as a date.
- [var dataValue: Data?](./datavalue.md)
  The value of the metadata item as a data value.
- [- statusOfValueForKey:error:](./statusofvalueforkey_error_.md)
  Reports whether the value for a given key is immediately available without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/loadvaluesasynchronouslyforkeys:completionhandler:)*