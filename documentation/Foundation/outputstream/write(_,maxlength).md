# write(_:maxLength:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the contents of a provided data buffer to the receiver.

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
func write(_ buffer: UnsafePointer<UInt8>, maxLength len: Int) -> Int
```

```objc
- (NSInteger) write:(const uint8_t *) buffer maxLength:(NSUInteger) len;
```

## Mentions

- [Uploading streams of data](../uploading-streams-of-data.md)

#### Return Value

A number indicating the outcome of the operation:

- A positive number indicates the number of bytes written.
- `0` indicates that a fixed-length stream and has reached its capacity.
- `-1` means that the operation failed; more information about the error can be obtained with [`streamError`](../stream/streamerror.md).

## Parameters

- `buffer`: The data to write.
- `len`: The length of the data buffer, in bytes.

  > ❗ **Important**:  The behavior of this method is undefined if you pass a negative or zero number.

## See Also

### Using Streams
- [var hasSpaceAvailable: Bool](./hasspaceavailable.md)
  A boolean value that indicates whether the receiver can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/write(_:maxlength:))*