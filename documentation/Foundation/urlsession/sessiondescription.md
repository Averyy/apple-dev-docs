# sessionDescription

**Framework**: Foundation  
**Kind**: property

An app-defined descriptive label for the session.

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
var sessionDescription: String? { get set }
```

## Mentions

- [Analyzing HTTP traffic with Instruments](analyzing-http-traffic-with-instruments.md)

#### Discussion

This property contains a human-readable string that you can use for debugging purposes. This value may be `nil` and defaults to `nil`. The value is ignored by the session.

## See Also

- [func finishTasksAndInvalidate()](urlsession/finishtasksandinvalidate.md)
  Invalidates the session, allowing any outstanding tasks to finish.
- [func flush(completionHandler: () -> Void)](urlsession/flush(completionhandler:).md)
  Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [func getTasksWithCompletionHandler(([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) -> Void)](urlsession/gettaskswithcompletionhandler(_:).md)
  Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [func getAllTasks(completionHandler: ([URLSessionTask]) -> Void)](urlsession/getalltasks(completionhandler:).md)
  Asynchronously calls a completion callback with all tasks in a session
- [func invalidateAndCancel()](urlsession/invalidateandcancel.md)
  Cancels all outstanding tasks and then invalidates the session.
- [func reset(completionHandler: () -> Void)](urlsession/reset(completionhandler:).md)
  Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/sessiondescription)*