# InputStream

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSInputStream : NSStream
```

## Mentions

- [Uploading streams of data](./uploading-streams-of-data.md)

#### Overview

[`InputStream`](./inputstream.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFReadStream`](../CoreFoundation/cfreadstream.md). For more information on toll-free bridging, see [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2).

##### Subclassing Notes

`NSInputStream` is an abstract superclass of a *class cluster* consisting of concrete subclasses of `NSStream` that provide standard read-only access to stream data. Although `NSInputStream` is probably sufficient for most situations requiring access to stream data, you can create a subclass of `NSInputStream` if you want more specialized behavior (for example, you want to record statistics on the data in a stream).

###### Methods to Override

To create a subclass of `NSInputStream` you may have to implement initializers for the type of stream data supported and suitably re-implement existing initializers. You must also provide complete implementations of the following methods:

- [`read(_:maxLength:)`](./inputstream/read%28_,maxlength%29.md)

From the current read index, take up to the number of bytes specified in the second parameter from the stream and place them in the client-supplied buffer (first parameter). The buffer must be of the size specified by the second parameter. Return the actual number of bytes placed in the buffer; if there is nothing left in the stream, return `0`. Reset the index into the stream for the next read operation.

- [`getBuffer(_:length:)`](./inputstream/getbuffer%28_,length%29.md)

Return in 0(1) a pointer to the subclass-allocated buffer (first parameter). Return by reference in the second parameter the number of bytes actually put into the buffer. The buffer’s contents are valid only until the next stream operation. Return [`false`](../Swift/false.md) if you cannot access data in the buffer; otherwise, return [`true`](../Swift/true.md). If this method is not appropriate for your type of stream, you may return [`false`](../Swift/false.md).

- [`hasBytesAvailable`](./inputstream/hasbytesavailable.md)

Return [`true`](../Swift/true.md) if there is more data to read in the stream, [`false`](../Swift/false.md) if there is not. If you want to be semantically compatible with `NSInputStream`, return [`true`](../Swift/true.md) if a read must be attempted to determine if bytes are available.

## Topics

### Creating Streams
- [init(data: Data)](./inputstream/init%28data%29.md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [convenience init?(fileAtPath: String)](./inputstream/init%28fileatpath%29.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [init?(url: URL)](./inputstream/init%28url%29-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
- [+ inputStreamWithData:](./nsinputstream/inputstreamwithdata_.md)
  Creates and returns an initialized `NSInputStream` object for reading from a given `NSData` object.
- [+ inputStreamWithFileAtPath:](./nsinputstream/inputstreamwithfileatpath_.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given path.
### Using Streams
- [func read(UnsafeMutablePointer<UInt8>, maxLength: Int) -> Int](./inputstream/read%28_,maxlength%29.md)
  Reads up to a given number of bytes into a given buffer.
- [func getBuffer(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length: UnsafeMutablePointer<Int>) -> Bool](./inputstream/getbuffer%28_,length%29.md)
  Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.
- [var hasBytesAvailable: Bool](./inputstream/hasbytesavailable.md)
  A Boolean value that indicates whether the receiver has bytes available to read.
### Initializers
- [init?(URL: URL)](./inputstream/init%28url%29-3lbto.md)
### Default Implementations
- [NSInputStream Implementations](./inputstream/nsinputstream-implementations.md)
### Type Methods
- [+ inputStreamWithURL:](./nsinputstream/inputstreamwithurl_.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given URL.

## Relationships

### Inherits From
- [Stream](./stream.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Streams
- [class Stream](./stream.md)
  An abstract class representing a stream.
- [class OutputStream](./outputstream.md)
  A stream that provides write-only stream functionality.
- [protocol StreamDelegate](./streamdelegate.md)
  An interface that delegates of a stream instance use to handle events on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream)*