# hasBytesAvailable

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver has bytes available to read.

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
var hasBytesAvailable: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver has bytes available to read, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). May also return [`true`](https://developer.apple.com/documentation/Swift/true) if a read must be attempted in order to determine the availability of bytes.

## See Also

- [func read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int](inputstream/read(_:maxlength:).md)
  Reads up to a given number of bytes into a given buffer.
- [func getBuffer(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length: UnsafeMutablePointer<Int>) -> Bool](inputstream/getbuffer(_:length:).md)
  Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/hasbytesavailable)*