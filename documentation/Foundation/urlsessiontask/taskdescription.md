# taskDescription

**Framework**: Foundation  
**Kind**: property

An app-provided string value for the current task.

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
var taskDescription: String? { get set }
```

#### Discussion

The system doesn’t interpret this value; use it for whatever purpose you see fit. For example, you could store a description of the task for debugging purposes, or a key to track the task in your own data structures.

## See Also

- [var currentRequest: URLRequest?](urlsessiontask/currentrequest.md)
  The URL request object currently being handled by the task.
- [var originalRequest: URLRequest?](urlsessiontask/originalrequest.md)
  The original request object passed when the task was created.
- [var response: URLResponse?](urlsessiontask/response.md)
  The server’s response to the currently active request.
- [var taskIdentifier: Int](urlsessiontask/taskidentifier.md)
  An identifier uniquely identifying the task within a given session.
- [var error: (any Error)?](urlsessiontask/error.md)
  An error object that indicates why the task failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/taskdescription)*