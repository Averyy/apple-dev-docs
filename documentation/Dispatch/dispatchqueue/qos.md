# qos

**Framework**: Dispatch  
**Kind**: property  
**Role**: Instance Property

The quality-of-service level assgined to the queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var qos: DispatchQoS { get }
```

## See Also

### Managing Queue Attributes
- [var label: String](./label.md)
  The label you assigned to the dispatch queue at creation time.
- [func setTarget(queue: dispatch_queue_t?)](../dispatchobject/settarget%28queue%29.md)
  Specifies the dispatch queue on which to perform work associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/qos)*