# getStreamsToHost(withName:port:inputStream:outputStream:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t in Network framework instead

## Declaration

```swift
class func getStreamsToHost(withName hostname: String, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

```objc
+ (void) getStreamsToHostWithName:(NSString *) hostname port:(NSInteger) port inputStream:(NSInputStream **) inputStream outputStream:(NSOutputStream **) outputStream;
```

## Parameters

- `hostname`: The host to which to connect.
- `port`: The port to connect to on `host`.
- `inputStream`: Upon return, contains the input stream. If `nil` is passed, the stream object is not created.
- `outputStream`: Upon return, contains the output stream. If `nil` is passed, the stream object is not created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/getstreamstohost(withname:port:inputstream:outputstream:))*