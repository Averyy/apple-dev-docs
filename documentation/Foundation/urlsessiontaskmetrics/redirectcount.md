# redirectCount

**Framework**: Foundation  
**Kind**: property

The number of redirects that occurred during the execution of the task.

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
var redirectCount: Int { get }
```

## See Also

- [var transactionMetrics: [URLSessionTaskTransactionMetrics]](urlsessiontaskmetrics/transactionmetrics.md)
  An array of metrics for each individual request-response transaction made during the execution of the task.
- [class URLSessionTaskTransactionMetrics](urlsessiontasktransactionmetrics.md)
  An object that encapsualtes the performance metrics collected by the URL Loading System during the execution of a session task.
- [var taskInterval: DateInterval](urlsessiontaskmetrics/taskinterval.md)
  The time interval between when a task is instantiated and when the task is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/redirectcount)*