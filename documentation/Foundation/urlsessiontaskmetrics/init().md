# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a task metrics instance.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.15
- tvOS 10.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 6.0

> **Deprecated**: Not supported

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Discussion

You should never need to create your own [`URLSessionTaskMetrics`](../urlsessiontaskmetrics.md) instances. If you are interested in task metrics, implement the [`urlSession(_:task:didFinishCollecting:)`](../urlsessiontaskdelegate/urlsession%28_,task,didfinishcollecting%29.md) method of [`URLSessionTaskDelegate`](../urlsessiontaskdelegate.md). The [`URLSession`](../urlsession.md) will collect task metrics for you and deliver them to this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/init())*