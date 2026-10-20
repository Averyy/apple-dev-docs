# getTasksWithCompletionHandler(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously calls a completion callback with all data, upload, and download tasks in a session.

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
func getTasksWithCompletionHandler(_ completionHandler: @escaping @Sendable ([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) -> Void)
```

```swift
var tasks: ([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) { get async }
```

```objc
- (void) getTasksWithCompletionHandler:(void (^)(NSArray<NSURLSessionDataTask *> *dataTasks, NSArray<NSURLSessionUploadTask *> *uploadTasks, NSArray<NSURLSessionDownloadTask *> *downloadTasks)) completionHandler;
```

#### Discussion

The arrays passed to the completion handler contain any tasks that you have created within the session, not including any tasks that have been invalidated after completing, failing, or being cancelled.

## Parameters

- `completionHandler`: The completion handler to call with the list of tasks. This handler is executed on the delegate queue.

## See Also

### Managing the session
- [func finishTasksAndInvalidate()](./finishtasksandinvalidate%28%29.md)
  Invalidates the session, allowing any outstanding tasks to finish.
- [func flush(completionHandler: () -> Void)](./flush%28completionhandler%29.md)
  Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [func getAllTasks(completionHandler: ([URLSessionTask]) -> Void)](./getalltasks%28completionhandler%29.md)
  Asynchronously calls a completion callback with all tasks in a session
- [func invalidateAndCancel()](./invalidateandcancel%28%29.md)
  Cancels all outstanding tasks and then invalidates the session.
- [func reset(completionHandler: () -> Void)](./reset%28completionhandler%29.md)
  Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [var sessionDescription: String?](./sessiondescription.md)
  An app-defined descriptive label for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/gettaskswithcompletionhandler(_:))*