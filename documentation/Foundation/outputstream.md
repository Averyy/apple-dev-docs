# OutputStream

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSOutputStream : NSStream
```

## Mentions

- [Uploading streams of data](./uploading-streams-of-data.md)

## Overview

[`OutputStream`](./outputstream.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFWriteStream`](../CoreFoundation/cfwritestream.md). For more information on toll-free bridging, see [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2).

### Subclassing Notes

`NSOutputStream` is a concrete subclass of `NSStream` that lets you write data to a stream. Although `NSOutputStream` is probably sufficient for most situations requiring this capability, you can create a subclass of `NSOutputStream` if you want more specialized behavior (for example, you want to record statistics on the data in a stream).

#### Methods to Override

To create a subclass of `NSOutputStream` you may have to implement initializers for the type of stream data supported and suitably reimplement existing initializers. You must also provide complete implementations of the following methods:

- [`write(_:maxLength:)`](./outputstream/write%28_,maxlength%29.md)

From the current write pointer, take up to the number of bytes specified in the `maxLength:` parameter from the client-supplied buffer (first parameter) and put them onto the stream. The buffer must be of the size specified by the second parameter. To prepare for the next operation, offset the write pointer by the number of bytes written. Return a signed integer based on the outcome of the current operation:

- If the write operation is successful, return the actual number of bytes put onto the stream.
- If the stream is of a fixed length and has reached its capacity, return `0`.
- If there was an error writing to the stream, return `-1`.
- [`hasSpaceAvailable`](./outputstream/hasspaceavailable.md)

Return [`true`](../Swift/true.md) if the stream can currently accept more data, [`false`](../Swift/false.md) if it cannot. If you want to be semantically compatible with `NSOutputStream`, return [`true`](../Swift/true.md) if a write must be attempted to determine if space is available.

## Topics

### Creating Streams
- [class func toMemory() -> Self](./outputstream/tomemory%28%29.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [init(toMemory: ())](./outputstream/init%28tomemory%29.md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](./outputstream/init%28tobuffer,capacity%29.md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](./outputstream/init%28tofileatpath,append%29.md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](./outputstream/init%28url,append%29-5soau.md)
  Returns an initialized output stream for writing to a specified URL.
- [+ outputStreamToBuffer:capacity:](./nsoutputstream/outputstreamtobuffer_capacity_.md)
  Creates and returns an initialized output stream that can write to a provided buffer.
- [+ outputStreamToFileAtPath:append:](./nsoutputstream/outputstreamtofileatpath_append_.md)
  Creates and returns an initialized output stream for writing to a specified file.
### Using Streams
- [var hasSpaceAvailable: Bool](./outputstream/hasspaceavailable.md)
  A boolean value that indicates whether the receiver can be written to.
- [func write(UnsafePointer<UInt8>, maxLength: Int) -> Int](./outputstream/write%28_,maxlength%29.md)
  Writes the contents of a provided data buffer to the receiver.
### Initializers
- [init?(URL: URL, append: Bool)](./outputstream/init%28url,append%29-4dpt1.md)
### Default Implementations
- [NSOutputStream Implementations](./outputstream/nsoutputstream-implementations.md)
### Type Methods
- [+ outputStreamWithURL:append:](./nsoutputstream/outputstreamwithurl_append_.md)
  Creates and returns an initialized output stream for writing to a specified URL.

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
- [class InputStream](./inputstream.md)
  A stream that provides read-only stream functionality.
- [protocol StreamDelegate](./streamdelegate.md)
  An interface that delegates of a stream instance use to handle events on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream)*