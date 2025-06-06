# response

**Framework**: Foundation  
**Kind**: property

The server’s response to the currently active request.

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
@NSCopying
var response: URLResponse? { get }
```

## Mentions

- [Downloading files from websites](downloading-files-from-websites.md)

#### Discussion

This object provides information about the request as provided by the server. This information always includes the original URL. It may also include an expected length, MIME type information, encoding information, a suggested filename, or a combination of these.

## See Also

- [var currentRequest: URLRequest?](urlsessiontask/currentrequest.md)
  The URL request object currently being handled by the task.
- [var originalRequest: URLRequest?](urlsessiontask/originalrequest.md)
  The original request object passed when the task was created.
- [var taskDescription: String?](urlsessiontask/taskdescription.md)
  An app-provided string value for the current task.
- [var taskIdentifier: Int](urlsessiontask/taskidentifier.md)
  An identifier uniquely identifying the task within a given session.
- [var error: (any Error)?](urlsessiontask/error.md)
  An error object that indicates why the task failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/response)*