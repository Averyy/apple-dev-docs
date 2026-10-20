# threadPriority

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The thread priority to use when executing the operation

**Availability**:
- iOS 4.0+ - Deprecated in 8.0
- iPadOS 4.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`qualityOfService`](./qualityofservice.md) instead.

## Declaration

```swift
var threadPriority: Double { get set }
```

```objc
@property double threadPriority;
```

## See Also

### Configuring the Execution Priority
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  The relative amount of importance for granting system resources to the operation.
- [var queuePriority: Operation.QueuePriority](./queuepriority-swift.property.md)
  The execution priority of the operation in an operation queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/threadpriority)*