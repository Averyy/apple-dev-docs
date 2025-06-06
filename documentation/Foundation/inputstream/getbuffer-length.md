# getBuffer(_:length:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the buffer is available, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Subclasses of `NSInputStream` may return [`false`](https://developer.apple.com/documentation/swift/false) if this operation is not appropriate for the stream type.

## Parameters

- `buffer`: Upon return, contains a pointer to a read buffer. The buffer is only valid until the next stream operation is performed.
- `len`: Upon return, contains the number of bytes available.

## See Also

- [func read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int](inputstream/read(_:maxlength:).md)
  Reads up to a given number of bytes into a given buffer.
- [var hasBytesAvailable: Bool](inputstream/hasbytesavailable.md)
  A Boolean value that indicates whether the receiver has bytes available to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/getbuffer(_:length:))*