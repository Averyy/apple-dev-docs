# getStreamsToHost(withName:port:inputStream:outputStream:)

**Framework**: Foundation  
**Kind**: method

Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func getStreamsToHost(withName hostname: String, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

## Parameters

- `hostname`: The host to which to connect.
- `port`: The port to connect to on `host`.
- `inputStream`: Upon return, contains the input stream. If `nil` is passed, the stream object is not created.
- `outputStream`: Upon return, contains the output stream. If `nil` is passed, the stream object is not created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/getstreamstohost(withname:port:inputstream:outputstream:))*