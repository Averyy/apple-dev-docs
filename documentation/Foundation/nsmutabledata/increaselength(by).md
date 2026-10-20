# increaseLength(by:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Increases the length of the receiver by a given number of bytes.

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
func increaseLength(by extraLength: Int)
```

```objc
- (void) increaseLengthBy:(NSUInteger) extraLength;
```

#### Discussion

The additional bytes are all set to `0`.

> ❗ **Important**:  Changing the length of a mutable data object invalidates any existing data pointers returned by the [`bytes`](../nsdata/bytes.md) or [`mutableBytes`](./mutablebytes.md) properties.

## Parameters

- `extraLength`: The number of bytes by which to increase the receiver’s length.

## See Also

### Related Documentation
- [var length: Int](./length.md)
  The number of bytes contained in the mutable data object.
### Adding Bytes
- [func append(UnsafeRawPointer, length: Int)](./append%28_,length%29.md)
  Appends to the receiver a given number of bytes from a given buffer.
- [func append(Data)](./append%28_%29.md)
  Appends the content of another data object to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/increaselength(by:))*