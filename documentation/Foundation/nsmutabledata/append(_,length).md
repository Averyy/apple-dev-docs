# append(_:length:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends to the receiver a given number of bytes from a given buffer.

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
func append(_ bytes: UnsafeRawPointer, length: Int)
```

```objc
- (void) appendBytes:(const void *) bytes length:(NSUInteger) length;
```

## Discussion

A sample using this method can be found in [Working With Mutable Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingMutableData.html#//apple_ref/doc/uid/20002150).

## Parameters

- `bytes`: A buffer containing data to append to the receiver’s content.
- `length`: The number of bytes from `bytes` to append.

## See Also

### Adding Bytes
- [func append(Data)](./append%28_%29.md)
  Appends the content of another data object to the receiver.
- [func increaseLength(by: Int)](./increaselength%28by%29.md)
  Increases the length of the receiver by a given number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/append(_:length:))*