# streamTask(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2
- iPadOS 9.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.11+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t in Network framework instead

## Declaration

```swift
func streamTask(with service: NetService) -> URLSessionStreamTask
```

```objc
- (NSURLSessionStreamTask *) streamTaskWithNetService:(NSNetService *) service;
```

## Return Value

The new session stream task.

## Discussion

After you create the task, you must start it by calling its [`resume()`](../urlsessiontask/resume%28%29.md) method.

## Parameters

- `service`: A [`NetService`](../netservice.md) object used to determine the endpoint of the TCP/IP connection. This network service is resolved before any data is read or written to the resulting stream task.

## See Also

### Adding stream tasks to a session
- [func streamTask(withHostName: String, port: Int) -> URLSessionStreamTask](./streamtask%28withhostname,port%29.md)
  Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [class URLSessionStreamTask](../urlsessionstreamtask.md)
  A URL session task that is stream-based.
- [protocol URLSessionStreamDelegate](../urlsessionstreamdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/streamtask(with:))*