# read(_:maxLength:)

**Framework**: Foundation  
**Kind**: method

Reads up to a given number of bytes into a given buffer.

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
func read(_ buffer: UnsafeMutablePointer<UInt8>, maxLength len: Int) -> Int
```

#### Return Value

A number indicating the outcome of the operation:

#### Discussion

- A positive number indicates the number of bytes read.
- `0` indicates that the end of the buffer was reached.
- `-1` means that the operation failed; more information about the error can be obtained with [`streamError`](stream/streamerror.md).

## Parameters

- `buffer`: A data buffer. The buffer must be large enough to contain the number of bytes specified by  .
- `len`: The maximum number of bytes to read.

## See Also

- [func getBuffer(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length: UnsafeMutablePointer<Int>) -> Bool](inputstream/getbuffer(_:length:).md)
  Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.
- [var hasBytesAvailable: Bool](inputstream/hasbytesavailable.md)
  A Boolean value that indicates whether the receiver has bytes available to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/read(_:maxlength:))*