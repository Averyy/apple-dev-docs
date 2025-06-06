# currentRequest

**Framework**: Foundation  
**Kind**: property

The URL request object currently being handled by the task.

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
var currentRequest: URLRequest? { get }
```

#### Discussion

This value is typically the same as the initial request ([`originalRequest`](urlsessiontask/originalrequest.md)) except when the server has responded to the initial request with a redirect to a different URL.

## See Also

- [var originalRequest: URLRequest?](urlsessiontask/originalrequest.md)
  The original request object passed when the task was created.
- [var response: URLResponse?](urlsessiontask/response.md)
  The server’s response to the currently active request.
- [var taskDescription: String?](urlsessiontask/taskdescription.md)
  An app-provided string value for the current task.
- [var taskIdentifier: Int](urlsessiontask/taskidentifier.md)
  An identifier uniquely identifying the task within a given session.
- [var error: (any Error)?](urlsessiontask/error.md)
  An error object that indicates why the task failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/currentrequest)*