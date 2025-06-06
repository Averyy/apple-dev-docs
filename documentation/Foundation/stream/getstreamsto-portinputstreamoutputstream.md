# getStreamsTo(_:port:inputStream:outputStream:)

**Framework**: Foundation  
**Kind**: method

Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class func getStreamsTo(_ host: Host, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

#### Discussion

If neither `port` nor `host` is properly specified, no socket connection is made.

## Parameters

- `host`: The host to which to connect.
- `port`: The port to connect to on  .
- `inputStream`: Upon return, contains the input stream. If   is passed, the stream object is not created.
- `outputStream`: Upon return, contains the output stream. If   is passed, the stream object is not created.

## See Also

- [Stream Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/getstreamsto(_:port:inputstream:outputstream:))*