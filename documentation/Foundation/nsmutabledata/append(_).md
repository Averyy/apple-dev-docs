# append(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends the content of another data object to the receiver.

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
func append(_ other: Data)
```

```objc
- (void) appendData:(NSData *) other;
```

## Parameters

- `other`: The data object whose content is to be appended to the contents of the receiver.

## See Also

### Adding Bytes
- [func append(UnsafeRawPointer, length: Int)](./append%28_,length%29.md)
  Appends to the receiver a given number of bytes from a given buffer.
- [func increaseLength(by: Int)](./increaselength%28by%29.md)
  Increases the length of the receiver by a given number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/append(_:))*