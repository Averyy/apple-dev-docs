# OutputStream

**Framework**: Foundation  
**Kind**: class

A stream that provides write-only stream functionality.

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
class OutputStream
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)

#### Overview

[`OutputStream`](outputstream.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFWriteStream`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStream). For more information on toll-free bridging, see [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2).

##### Subclassing Notes

`NSOutputStream` is a concrete subclass of `NSStream` that lets you write data to a stream. Although `NSOutputStream` is probably sufficient for most situations requiring this capability, you can create a subclass of `NSOutputStream` if you want more specialized behavior (for example, you want to record statistics on the data in a stream).

###### Methods to Override

To create a subclass of `NSOutputStream` you may have to implement initializers for the type of stream data supported and suitably reimplement existing initializers. You must also provide complete implementations of the following methods:

- [`write(_:maxLength:)`](outputstream/write(_:maxlength:).md)

From the current write pointer, take up to the number of bytes specified in the `maxLength:` parameter from the client-supplied buffer (first parameter) and put them onto the stream. The buffer must be of the size specified by the second parameter. To prepare for the next operation, offset the write pointer by the number of bytes written. Return a signed integer based on the outcome of the current operation:

- If the write operation is successful, return the actual number of bytes put onto the stream.
- If the stream is of a fixed length and has reached its capacity, return `0`.
- If there was an error writing to the stream, return `-1`.
- [`hasSpaceAvailable`](outputstream/hasspaceavailable.md)

Return [`true`](https://developer.apple.com/documentation/Swift/true) if the stream can currently accept more data, [`false`](https://developer.apple.com/documentation/Swift/false) if it cannot. If you want to be semantically compatible with `NSOutputStream`, return [`true`](https://developer.apple.com/documentation/Swift/true) if a write must be attempted to determine if space is available.

## Topics

### Creating Streams
- [class func toMemory() -> Self](outputstream/tomemory.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [convenience init?(URL: URL, append: Bool)](outputstream/init(url:append:)-8e5le.md)
  Creates and returns an initialized output stream for writing to a specified URL.
- [init(toMemory: ())](outputstream/init(tomemory:).md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](outputstream/init(tobuffer:capacity:).md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](outputstream/init(tofileatpath:append:).md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](outputstream/init(url:append:)-5soau.md)
  Returns an initialized output stream for writing to a specified URL.
### Using Streams
- [var hasSpaceAvailable: Bool](outputstream/hasspaceavailable.md)
  A boolean value that indicates whether the receiver can be written to.
- [func write(UnsafePointer<UInt8>, maxLength: Int) -> Int](outputstream/write(_:maxlength:).md)
  Writes the contents of a provided data buffer to the receiver.

## Relationships

### Inherits From
- [Stream](stream.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class Stream](stream.md)
  An abstract class representing a stream.
- [class InputStream](inputstream.md)
  A stream that provides read-only stream functionality.
- [protocol StreamDelegate](streamdelegate.md)
  An interface that delegates of a stream instance use to handle events on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream)*