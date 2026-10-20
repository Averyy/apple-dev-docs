# URLSessionTaskMetrics

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object encapsulating the metrics for a session task.

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
class URLSessionTaskMetrics
```

```objc
@interface NSURLSessionTaskMetrics : NSObject
```

#### Overview

Each [`URLSessionTaskMetrics`](./urlsessiontaskmetrics.md) object contains the [`taskInterval`](./urlsessiontaskmetrics/taskinterval.md) and [`redirectCount`](./urlsessiontaskmetrics/redirectcount.md), as well as metrics for each request-and-response transaction made during the execution of the task.

## Topics

### Creating task metrics
- [init()](./urlsessiontaskmetrics/init%28%29.md)
  Creates a task metrics instance.
### Accessing task metrics
- [var transactionMetrics: [URLSessionTaskTransactionMetrics]](./urlsessiontaskmetrics/transactionmetrics.md)
  An array of metrics for each individual request-response transaction made during the execution of the task.
- [class URLSessionTaskTransactionMetrics](./urlsessiontasktransactionmetrics.md)
  An object that encapsualtes the performance metrics collected by the URL Loading System during the execution of a session task.
- [var taskInterval: DateInterval](./urlsessiontaskmetrics/taskinterval.md)
  The time interval between when a task is instantiated and when the task is completed.
- [var redirectCount: Int](./urlsessiontaskmetrics/redirectcount.md)
  The number of redirects that occurred during the execution of the task.
### Type Methods
- [class func new() -> Self](./urlsessiontaskmetrics/new%28%29.md)
  Creates a task metrics instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Collecting task metrics
- [func urlSession(URLSession, task: URLSessionTask, didFinishCollecting: URLSessionTaskMetrics)](./urlsessiontaskdelegate/urlsession%28_,task,didfinishcollecting%29.md)
  Tells the delegate that the session finished collecting metrics for the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics)*