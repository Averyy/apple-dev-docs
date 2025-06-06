# dataTask(with:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func dataTask(with request: URLRequest, completionHandler: @escaping (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask
```

#### Return Value

The new session data task.

#### Discussion

By creating a task based on a request object, you can tune various aspects of the task’s behavior, including the cache policy and timeout interval.

By using the completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting [`NSData`](nsdata.md), [`URLResponse`](urlresponse.md), and [`NSError`](nserror.md) objects inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

You should pass a `nil` completion handler  when creating tasks in sessions whose delegates include a [`urlSession(_:dataTask:didReceive:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md) method.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

If the request completes successfully, the `data` parameter of the completion handler block contains the resource data, and the `error` parameter is `nil`. If the request fails, the `data` parameter is `nil` and the `error` parameter contain information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

## Parameters

- `request`: A URL request object that provides the URL, cache policy, request type, body data or body stream, and so on.
- `completionHandler`: This completion handler takes the following parameters:

## See Also

- [func dataTask(with: URL) -> URLSessionDataTask](urlsession/datatask(with:)-10dy7.md)
  Creates a task that retrieves the contents of the specified URL.
- [func dataTask(with: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-52wk8.md)
  Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [func dataTask(with: URLRequest) -> URLSessionDataTask](urlsession/datatask(with:)-7jpys.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [class URLSessionDataTask](urlsessiondatatask.md)
  A URL session task that returns downloaded data directly to the app in memory.
- [protocol URLSessionDataDelegate](urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/datatask(with:completionhandler:)-e6xv)*