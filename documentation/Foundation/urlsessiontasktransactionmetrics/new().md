# new()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a new transaction metrics instance.

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
class func new() -> Self
```

```objc
+ (instancetype) new;
```

## Discussion

You should never need to create your own [`URLSessionTaskTransactionMetrics`](../urlsessiontasktransactionmetrics.md) instances. The [`URLSession`](../urlsession.md) creates task transaction metrics as part of the [`URLSessionTaskMetrics`](../urlsessiontaskmetrics.md) instance that it delivers to the [`urlSession(_:task:didFinishCollecting:)`](../urlsessiontaskdelegate/urlsession%28_,task,didfinishcollecting%29.md) method of [`URLSessionTaskDelegate`](../urlsessiontaskdelegate.md).

## See Also

### Creating transaction metrics
- [init()](./init%28%29.md)
  Creates a transaction metrics instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/new())*