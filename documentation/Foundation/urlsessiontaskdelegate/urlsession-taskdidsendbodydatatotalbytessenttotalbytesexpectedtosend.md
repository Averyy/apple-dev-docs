# urlSession(_:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:)

**Framework**: Foundation  
**Kind**: method

Periodically informs the delegate of the progress of sending body content to the server.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)
```

#### Discussion

The `totalBytesSent` and `totalBytesExpectedToSend` parameters are also available as [`URLSessionTask`](urlsessiontask.md) properties [`countOfBytesSent`](urlsessiontask/countofbytessent.md) and [`countOfBytesExpectedToSend`](urlsessiontask/countofbytesexpectedtosend.md). Or, since [`URLSessionTask`](urlsessiontask.md) supports [`ProgressReporting`](progressreporting.md), you can use the task’s [`progress`](urlsessiontask/progress.md) property instead, which may be more convenient.

## Parameters

- `session`: The session containing the data task.
- `task`: The data task.
- `bytesSent`: The number of bytes sent since the last time this delegate method was called.
- `totalBytesSent`: The total number of bytes sent so far.
- `totalBytesExpectedToSend`: Otherwise, the value is   ( ) if you provided a stream or body data object, or zero ( ) if you did not.

## See Also

- [func urlSession(URLSession, task: URLSessionTask, needNewBodyStream: (InputStream?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:neednewbodystream:).md)
  Tells the delegate when a task requires a new request body stream to send to the remote server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:))*