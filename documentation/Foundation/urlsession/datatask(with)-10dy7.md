# dataTask(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a task that retrieves the contents of the specified URL.

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
func dataTask(with url: URL) -> URLSessionDataTask
```

```objc
- (NSURLSessionDataTask *) dataTaskWithURL:(NSURL *) url;
```

## Mentions

- [Fetching website data into memory](../fetching-website-data-into-memory.md)

#### Return Value

The new session data task.

#### Discussion

After you create the task, you must start it by calling its [`resume()`](../urlsessiontask/resume%28%29.md) method. The task calls methods on the session’s delegate to provide you with the response metadata, response data, and so on.

## Parameters

- `url`: The URL to be retrieved.

## See Also

### Adding data tasks to a session
- [func dataTask(with: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](./datatask%28with,completionhandler%29-52wk8.md)
  Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [func dataTask(with: URLRequest) -> URLSessionDataTask](./datatask%28with%29-7jpys.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [func dataTask(with: URLRequest, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](./datatask%28with,completionhandler%29-e6xv.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [class URLSessionDataTask](../urlsessiondatatask.md)
  A URL session task that returns downloaded data directly to the app in memory.
- [protocol URLSessionDataDelegate](../urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/datatask(with:)-10dy7)*