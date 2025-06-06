# streamTask(withHostName:port:)

**Framework**: Foundation  
**Kind**: method

Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func streamTask(withHostName hostname: String, port: Int) -> URLSessionStreamTask
```

#### Return Value

The new session stream task.

#### Discussion

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

## Parameters

- `hostname`: The hostname of the connection endpoint.
- `port`: The port of the connection endpoint.

## See Also

- [func streamTask(with: NetService) -> URLSessionStreamTask](urlsession/streamtask(with:).md)
  Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.
- [class URLSessionStreamTask](urlsessionstreamtask.md)
  A URL session task that is stream-based.
- [protocol URLSessionStreamDelegate](urlsessionstreamdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/streamtask(withhostname:port:))*