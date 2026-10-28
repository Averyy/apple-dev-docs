# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A delegate specific to the task.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var delegate: (any URLSessionTaskDelegate)? { get set }
```

```objc
@property (retain, nullable) id<NSURLSessionTaskDelegate> delegate;
```

## Discussion

This task-specific delegate receives messages from the task before the session’s [`delegate`](../urlsession/delegate.md) receives them. This is similar to the behavior of the `delegate` parameter used by the asychronous methods in [`URLSession`](../urlsession.md) like [`bytes(for:delegate:)`](../urlsession/bytes%28for,delegate%29.md) and [`data(for:delegate:)`](../urlsession/data%28for,delegate%29.md).

## See Also

### Using a task-specific delegate
- [protocol URLSessionTaskDelegate](../urlsessiontaskdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/delegate)*