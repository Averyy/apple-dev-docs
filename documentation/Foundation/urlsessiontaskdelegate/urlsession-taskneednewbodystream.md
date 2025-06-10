# urlSession(_:task:needNewBodyStream:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate when a task requires a new request body stream to send to the remote server.

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
optional func urlSession(_ session: URLSession, needNewBodyStreamForTask task: URLSessionTask) async -> InputStream?
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)

#### Discussion

The task calls this delegate method under two circumstances:

- To provide the initial request body stream if the task was created with [`uploadTask(withStreamedRequest:)`](urlsession/uploadtask(withstreamedrequest:).md)
- To provide a replacement request body stream if the task needs to resend a request that has a body stream because of an authentication challenge or other recoverable server error.

> **Note**:  You don’t need to implement this method if your code provides the request body using a file URL or a data object.

## Parameters

- `session`: The session containing the task that needs a new body stream.
- `task`: The task that needs a new body stream.
- `completionHandler`: A completion handler that your delegate method should call with the new body stream.

## See Also

- [func urlSession(URLSession, task: URLSessionTask, didSendBodyData: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)](urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:).md)
  Periodically informs the delegate of the progress of sending body content to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:neednewbodystream:))*