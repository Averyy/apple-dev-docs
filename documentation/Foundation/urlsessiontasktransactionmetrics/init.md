# init()

**Framework**: Foundation  
**Kind**: init

Creates a transaction metrics instance.

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

You should never need to create your own [`URLSessionTaskTransactionMetrics`](urlsessiontasktransactionmetrics.md) instances. The [`URLSession`](urlsession.md) creates task transaction metrics as part of the [`URLSessionTaskMetrics`](urlsessiontaskmetrics.md) instance that it delivers to the [`urlSession(_:task:didFinishCollecting:)`](urlsessiontaskdelegate/urlsession(_:task:didfinishcollecting:).md) method of [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md).

## See Also

- [class func new() -> Self](urlsessiontasktransactionmetrics/new.md)
  Creates a new transaction metrics instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/init())*