# getAllTasks(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously calls a completion callback with all tasks in a session

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
func getAllTasks(completionHandler: @escaping @Sendable ([URLSessionTask]) -> Void)
```

```swift
var allTasks: [URLSessionTask] { get async }
```

```objc
- (void) getAllTasksWithCompletionHandler:(void (^)(NSArray<__kindof NSURLSessionTask *> *tasks)) completionHandler;
```

## Parameters

- `completionHandler`: The completion handler to call with the list of tasks.

## See Also

### Managing the session
- [func finishTasksAndInvalidate()](./finishtasksandinvalidate%28%29.md)
  Invalidates the session, allowing any outstanding tasks to finish.
- [func flush(completionHandler: () -> Void)](./flush%28completionhandler%29.md)
  Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [func getTasksWithCompletionHandler(([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) -> Void)](./gettaskswithcompletionhandler%28_%29.md)
  Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [func invalidateAndCancel()](./invalidateandcancel%28%29.md)
  Cancels all outstanding tasks and then invalidates the session.
- [func reset(completionHandler: () -> Void)](./reset%28completionhandler%29.md)
  Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [var sessionDescription: String?](./sessiondescription.md)
  An app-defined descriptive label for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/getalltasks(completionhandler:))*