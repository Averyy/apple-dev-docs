# error

**Framework**: Foundation  
**Kind**: property

An error object that indicates why the task failed.

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
var error: (any Error)? { get }
```

#### Discussion

This value is `nil` if the task is still active or if the transfer completed successfully.

## See Also

- [var currentRequest: URLRequest?](urlsessiontask/currentrequest.md)
  The URL request object currently being handled by the task.
- [var originalRequest: URLRequest?](urlsessiontask/originalrequest.md)
  The original request object passed when the task was created.
- [var response: URLResponse?](urlsessiontask/response.md)
  The server’s response to the currently active request.
- [var taskDescription: String?](urlsessiontask/taskdescription.md)
  An app-provided string value for the current task.
- [var taskIdentifier: Int](urlsessiontask/taskidentifier.md)
  An identifier uniquely identifying the task within a given session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/error)*