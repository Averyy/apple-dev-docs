# taskIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An identifier uniquely identifying the task within a given session.

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
var taskIdentifier: Int { get }
```

```objc
@property (readonly) NSUInteger taskIdentifier;
```

#### Discussion

This value is unique only within the context of a single session; tasks in other sessions may have the same [`taskIdentifier`](./taskidentifier.md) value.

## See Also

### Obtaining general task information
- [var currentRequest: URLRequest?](./currentrequest.md)
  The URL request object currently being handled by the task.
- [var originalRequest: URLRequest?](./originalrequest.md)
  The original request object passed when the task was created.
- [var response: URLResponse?](./response.md)
  The server’s response to the currently active request.
- [var taskDescription: String?](./taskdescription.md)
  An app-provided string value for the current task.
- [var error: (any Error)?](./error.md)
  An error object that indicates why the task failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/taskidentifier)*