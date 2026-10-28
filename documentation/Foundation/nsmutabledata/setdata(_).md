# setData(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the entire contents of the receiver with the contents of another data object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setData(_ data: Data)
```

```objc
- (void) setData:(NSData *) data;
```

## Discussion

As part of its implementation, this method calls [`replaceBytes(in:withBytes:)`](./replacebytes%28in,withbytes%29.md).

## Parameters

- `data`: The data object whose content replaces that of the receiver.

## See Also

### Modifying Bytes
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer)](./replacebytes%28in,withbytes%29.md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer?, length: Int)](./replacebytes%28in,withbytes,length%29.md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func resetBytes(in: NSRange)](./resetbytes%28in%29.md)
  Replaces with zeroes the contents of the receiver in a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/setdata(_:))*