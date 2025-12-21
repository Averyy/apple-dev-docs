# InputStream

**Framework**: Foundation  
**Kind**: class

A stream that provides read-only stream functionality.

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
class InputStream
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)

#### Overview

[`InputStream`](inputstream.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFReadStream`](https://developer.apple.com/documentation/CoreFoundation/CFReadStream). For more information on toll-free bridging, see [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2).

##### Subclassing Notes

`NSInputStream` is an abstract superclass of a  consisting of concrete subclasses of `NSStream` that provide standard read-only access to stream data. Although `NSInputStream` is probably sufficient for most situations requiring access to stream data, you can create a subclass of `NSInputStream` if you want more specialized behavior (for example, you want to record statistics on the data in a stream).

###### Methods to Override

To create a subclass of `NSInputStream` you may have to implement initializers for the type of stream data supported and suitably re-implement existing initializers. You must also provide complete implementations of the following methods:

- [`read(_:maxLength:)`](inputstream/read(_:maxlength:).md)

From the current read index, take up to the number of bytes specified in the second parameter from the stream and place them in the client-supplied buffer (first parameter). The buffer must be of the size specified by the second parameter. Return the actual number of bytes placed in the buffer; if there is nothing left in the stream, return `0`. Reset the index into the stream for the next read operation.

- [`getBuffer(_:length:)`](inputstream/getbuffer(_:length:).md)

Return in 0(1) a pointer to the subclass-allocated buffer (first parameter). Return by reference in the second parameter the number of bytes actually put into the buffer. The buffer’s contents are valid only until the next stream operation. Return [`false`](https://developer.apple.com/documentation/Swift/false) if you cannot access data in the buffer; otherwise, return [`true`](https://developer.apple.com/documentation/Swift/true). If this method is not appropriate for your type of stream, you may return [`false`](https://developer.apple.com/documentation/Swift/false).

- [`hasBytesAvailable`](inputstream/hasbytesavailable.md)

Return [`true`](https://developer.apple.com/documentation/Swift/true) if there is more data to read in the stream, [`false`](https://developer.apple.com/documentation/Swift/false) if there is not. If you want to be semantically compatible with `NSInputStream`, return [`true`](https://developer.apple.com/documentation/Swift/true) if a read must be attempted to determine if bytes are available.

## Topics

### Creating Streams
- [convenience init?(URL: URL)](inputstream/init(url:)-y5k.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given URL.
- [init(data: Data)](inputstream/init(data:).md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [convenience init?(fileAtPath: String)](inputstream/init(fileatpath:).md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [init?(url: URL)](inputstream/init(url:)-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
### Using Streams
- [func read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int](inputstream/read(_:maxlength:).md)
  Reads up to a given number of bytes into a given buffer.
- [func getBuffer(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length: UnsafeMutablePointer<Int>) -> Bool](inputstream/getbuffer(_:length:).md)
  Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.
- [var hasBytesAvailable: Bool](inputstream/hasbytesavailable.md)
  A Boolean value that indicates whether the receiver has bytes available to read.

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
- [class OutputStream](outputstream.md)
  A stream that provides write-only stream functionality.
- [protocol StreamDelegate](streamdelegate.md)
  An interface that delegates of a stream instance use to handle events on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream)*