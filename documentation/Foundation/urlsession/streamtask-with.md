# streamTask(with:)

**Framework**: Foundation  
**Kind**: method

Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func streamTask(with service: NetService) -> URLSessionStreamTask
```

#### Return Value

The new session stream task.

#### Discussion

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

## Parameters

- `service`: A   object used to determine the endpoint of the TCP/IP connection. This network service is resolved before any data is read or written to the resulting stream task.

## See Also

- [func streamTask(withHostName: String, port: Int) -> URLSessionStreamTask](urlsession/streamtask(withhostname:port:).md)
  Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [class URLSessionStreamTask](urlsessionstreamtask.md)
  A URL session task that is stream-based.
- [protocol URLSessionStreamDelegate](urlsessionstreamdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/streamtask(with:))*