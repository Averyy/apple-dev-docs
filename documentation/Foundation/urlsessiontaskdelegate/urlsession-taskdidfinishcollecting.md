# urlSession(_:task:didFinishCollecting:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the session finished collecting metrics for the task.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didFinishCollecting metrics: URLSessionTaskMetrics)
```

## Parameters

- `session`: The session collecting the metrics.
- `task`: The task whose metrics have been collected.
- `metrics`: The collected metrics.

## See Also

- [class URLSessionTaskMetrics](urlsessiontaskmetrics.md)
  An object encapsulating the metrics for a session task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didfinishcollecting:))*