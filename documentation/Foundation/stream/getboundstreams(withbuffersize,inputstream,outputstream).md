# getBoundStreams(withBufferSize:inputStream:outputStream:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns by reference a bound pair of input and output streams.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func getBoundStreams(withBufferSize bufferSize: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

```objc
+ (void) getBoundStreamsWithBufferSize:(NSUInteger) bufferSize inputStream:(NSInputStream **) inputStream outputStream:(NSOutputStream **) outputStream;
```

## Mentions

- [Uploading streams of data](../uploading-streams-of-data.md)

#### Discussion

The created streams are bound to one another, such that any data written to `outputStream` is received by `inputStream`.

This is a convenience method for calling [`CFStreamCreateBoundPair(_:_:_:_:)`](../../CoreFoundation/cfstreamcreateboundpair%28_,_,_,_%29.md) and bridging from the returned Core Foundation types.

## Parameters

- `bufferSize`: The size of the buffer, in bytes, used to transfer data from `inputStream` to `outputStream`.
- `inputStream`: On return, contains an input stream.
- `outputStream`: On return, contains an output stream.

## See Also

### Related Documentation
- [func CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, CFIndex)](../../CoreFoundation/cfstreamcreateboundpair%28_,_,_,_%29.md)
  Creates a bound pair of read and write streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/getboundstreams(withbuffersize:inputstream:outputstream:))*