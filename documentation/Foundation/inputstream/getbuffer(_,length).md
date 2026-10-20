# getBuffer(_:length:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.

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
func getBuffer(_ buffer: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length len: UnsafeMutablePointer<Int>) -> Bool
```

```objc
- (BOOL) getBuffer:(uint8_t **) buffer length:(NSUInteger *) len;
```

#### Return Value

[`true`](../../Swift/true.md) if the buffer is available, otherwise [`false`](../../Swift/false.md).

#### Discussion

Subclasses of `NSInputStream` may return [`false`](../../Swift/false.md) if this operation is not appropriate for the stream type.

## Parameters

- `buffer`: Upon return, contains a pointer to a read buffer. The buffer is only valid until the next stream operation is performed.
- `len`: Upon return, contains the number of bytes available.

## See Also

### Using Streams
- [func read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int](./read%28_,maxlength%29.md)
  Reads up to a given number of bytes into a given buffer.
- [var hasBytesAvailable: Bool](./hasbytesavailable.md)
  A Boolean value that indicates whether the receiver has bytes available to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/getbuffer(_:length:))*