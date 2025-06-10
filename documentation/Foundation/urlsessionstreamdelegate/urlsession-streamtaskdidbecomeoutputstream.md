# urlSession(_:streamTask:didBecome:outputStream:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the stream task has been completed as a result of the stream task calling the [`captureStreams()`](urlsessionstreamtask/capturestreams().md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, streamTask: URLSessionStreamTask, didBecome inputStream: InputStream, outputStream: OutputStream)
```

#### Discussion

This delegate method will only be called after all enqueued reads and writes for the stream task have been completed.

## Parameters

- `session`: The session of the stream task that has been completed.
- `streamTask`: The stream task that has been completed.
- `inputStream`: The created input stream. This   object is unopened.
- `outputStream`: The created output stream. This   object is unopened


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:streamtask:didbecome:outputstream:))*