# init()

**Framework**: Foundation  
**Kind**: init

Creates a task metrics instance.

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
init()
```

#### Discussion

You should never need to create your own [`URLSessionTaskMetrics`](urlsessiontaskmetrics.md) instances. If you are interested in task metrics, implement the [`urlSession(_:task:didFinishCollecting:)`](urlsessiontaskdelegate/urlsession(_:task:didfinishcollecting:).md) method of [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md). The [`URLSession`](urlsession.md) will collect task metrics for you and deliver them to this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/init())*