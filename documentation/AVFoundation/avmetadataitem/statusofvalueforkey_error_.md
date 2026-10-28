# statusOfValueForKey:error:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Reports whether the value for a given key is immediately available without blocking.

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
- (AVKeyValueStatus) statusOfValueForKey:(NSString *) key error:(NSError **) outError;
```

## Return Value

The current loading status of the value for `key`.

## Discussion

For full discussion, see [`AVAsynchronousKeyValueLoading`](../avasynchronouskeyvalueloading.md).

## Parameters

- `key`: The key whose status you want.
- `outError`: If the status of the value for the key is [`AVKeyValueStatus.failed`](../avkeyvaluestatus/failed.md), upon return contains an [`NSError`](../../Foundation/nserror.md) object that describes the failure that occurred.

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
- [- loadValuesAsynchronouslyForKeys:completionHandler:](./loadvaluesasynchronouslyforkeys_completionhandler_.md)
  Tells the object to load the values of any of the specified keys that aren’t already loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/statusofvalueforkey:error:)*