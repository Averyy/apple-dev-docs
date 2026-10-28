# hasBytesAvailable

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL hasBytesAvailable;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver has bytes available to read, otherwise [`false`](../../Swift/false.md). May also return [`true`](../../Swift/true.md) if a read must be attempted in order to determine the availability of bytes.

## See Also

### Using Streams
- [func read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int](./read%28_,maxlength%29.md)
  Reads up to a given number of bytes into a given buffer.
- [func getBuffer(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length: UnsafeMutablePointer<Int>) -> Bool](./getbuffer%28_,length%29.md)
  Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/hasbytesavailable)*