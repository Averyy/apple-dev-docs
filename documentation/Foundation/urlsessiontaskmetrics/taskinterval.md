# taskInterval

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The time interval between when a task is instantiated and when the task is completed.

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
var taskInterval: DateInterval { get }
```

```objc
@property (copy, readonly) NSDateInterval * taskInterval;
```

## See Also

### Accessing task metrics
- [var transactionMetrics: [URLSessionTaskTransactionMetrics]](./transactionmetrics.md)
  An array of metrics for each individual request-response transaction made during the execution of the task.
- [class URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)
  An object that encapsualtes the performance metrics collected by the URL Loading System during the execution of a session task.
- [var redirectCount: Int](./redirectcount.md)
  The number of redirects that occurred during the execution of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/taskinterval)*