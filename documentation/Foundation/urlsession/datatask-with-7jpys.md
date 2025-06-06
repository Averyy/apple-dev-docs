# dataTask(with:)

**Framework**: Foundation  
**Kind**: method

Creates a task that retrieves the contents of a URL based on the specified URL request object.

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
func dataTask(with request: URLRequest) -> URLSessionDataTask
```

#### Return Value

The new session data task.

#### Discussion

By creating a task based on a request object, you can tune various aspects of the task’s behavior, including the cache policy and timeout interval.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

## Parameters

- `request`: A URL request object that provides request-specific information such as the URL, cache policy, request type, and body data or body stream.

## See Also

- [func dataTask(with: URL) -> URLSessionDataTask](urlsession/datatask(with:)-10dy7.md)
  Creates a task that retrieves the contents of the specified URL.
- [func dataTask(with: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-52wk8.md)
  Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [func dataTask(with: URLRequest, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-e6xv.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [class URLSessionDataTask](urlsessiondatatask.md)
  A URL session task that returns downloaded data directly to the app in memory.
- [protocol URLSessionDataDelegate](urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/datatask(with:)-7jpys)*