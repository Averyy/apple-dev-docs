# queuePriority

**Framework**: Foundation  
**Kind**: property

The execution priority of the operation in an operation queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var queuePriority: Operation.QueuePriority { get set }
```

#### Discussion

This property contains the relative priority of the operation. This value is used to influence the order in which operations are dequeued and executed. The returned value always corresponds to one of the predefined constants. (For a list of valid values, see [`Operation.QueuePriority`](operation/queuepriority-swift.enum.md).) If no priority is explicitly set, this method returns `NSOperationQueuePriorityNormal`.

You should use priority values only as needed to classify the relative priority of non-dependent operations. Priority values should not be used to implement dependency management among different operation objects. If you need to establish dependencies between operations, use the [`addDependency(_:)`](operation/adddependency(_:).md) method instead.

If you attempt to specify a priority value that does not match one of the defined constants, the operation object automatically adjusts the value you specify towards the `NSOperationQueuePriorityNormal` priority, stopping at the first valid constant value. For example, if you specified the value -10, the operation would adjust that value to match the `NSOperationQueuePriorityVeryLow` constant. Similarly, if you specified +10, this operation would adjust the value to match the `NSOperationQueuePriorityVeryHigh` constant.

## See Also

- [var qualityOfService: QualityOfService](operation/qualityofservice.md)
  The relative amount of importance for granting system resources to the operation.
- [var threadPriority: Double](operation/threadpriority.md)
  The thread priority to use when executing the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/queuepriority-swift.property)*