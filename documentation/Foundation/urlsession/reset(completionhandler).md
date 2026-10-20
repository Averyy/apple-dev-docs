# reset(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.

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
func reset(completionHandler: @escaping @Sendable () -> Void)
```

```swift
func reset() async
```

```objc
- (void) resetWithCompletionHandler:(void (^)()) completionHandler;
```

## Parameters

- `completionHandler`: The completion handler to call when the reset operation is complete. This handler is executed on the delegate queue.

## See Also

### Managing the session
- [func finishTasksAndInvalidate()](./finishtasksandinvalidate%28%29.md)
  Invalidates the session, allowing any outstanding tasks to finish.
- [func flush(completionHandler: () -> Void)](./flush%28completionhandler%29.md)
  Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [func getTasksWithCompletionHandler(([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) -> Void)](./gettaskswithcompletionhandler%28_%29.md)
  Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [func getAllTasks(completionHandler: ([URLSessionTask]) -> Void)](./getalltasks%28completionhandler%29.md)
  Asynchronously calls a completion callback with all tasks in a session
- [func invalidateAndCancel()](./invalidateandcancel%28%29.md)
  Cancels all outstanding tasks and then invalidates the session.
- [var sessionDescription: String?](./sessiondescription.md)
  An app-defined descriptive label for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/reset(completionhandler:))*