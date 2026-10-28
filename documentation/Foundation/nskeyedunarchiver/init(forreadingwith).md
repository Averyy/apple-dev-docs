# init(forReadingWith:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an archiver to decode data from the specified location.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use [`init(forReadingFrom:)`](./init%28forreadingfrom%29.md) instead.

## Declaration

```swift
init(forReadingWith data: Data)
```

```objc
- (instancetype) initForReadingWithData:(NSData *) data;
```

## Return Value

An [`NSKeyedUnarchiver`](../nskeyedunarchiver.md) object initialized for for decoding `data`.

## Discussion

When you finish decoding data, you should invoke [`finishDecoding()`](./finishdecoding%28%29.md).

This method throws an exception if `data` is not a valid archive.

## Parameters

- `data`: An archive previously encoded by [`NSKeyedArchiver`](../nskeyedarchiver.md).

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
### Creating a Keyed Unarchiver
- [init(forReadingFrom: Data) throws](./init%28forreadingfrom%29.md)
  Initializes an archiver to decode data from the specified location.
- [init()](./init%28%29.md)
  Initializes an archiver to decode data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/init(forreadingwith:))*