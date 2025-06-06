# progress

**Framework**: Foundation  
**Kind**: property

An object that represents the total progress of the operations executing in the queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var progress: Progress { get }
```

#### Discussion

By default, [`OperationQueue`](operationqueue.md) doesn’t report progress until [`totalUnitCount`](progress/totalunitcount.md) is set. When [`totalUnitCount`](progress/totalunitcount.md) is set, the queue begins reporting progress. Each operation in the queue contributes one unit of completion to the overall progress of the queue for operations that are finished by the end of [`main()`](operation/main().md). Operations that override [`start()`](operation/start().md) and don’t invoke super don’t contribute to the queue’s progress.

> ⚠️ **Warning**:  Be careful to avoid race conditions and backward progress when updating [`totalUnitCount`](progress/totalunitcount.md). Consider a queue with a progress that has a [`completedUnitCount`](progress/completedunitcount.md) equal to `5` and a [`totalUnitCount`](progress/totalunitcount.md) equal to `10`, representing 50% completion. If you add 90 more operations to the queue, the [`totalUnitCount`](progress/totalunitcount.md) is now `100`, and the progress completion reports 5%. If the progress object is connected to a progress bar, the bar would visibly jump backward from 50% to 5%, which may not be desirable.

 Be careful to avoid race conditions and backward progress when updating [`totalUnitCount`](progress/totalunitcount.md). Consider a queue with a progress that has a [`completedUnitCount`](progress/completedunitcount.md) equal to `5` and a [`totalUnitCount`](progress/totalunitcount.md) equal to `10`, representing 50% completion. If you add 90 more operations to the queue, the [`totalUnitCount`](progress/totalunitcount.md) is now `100`, and the progress completion reports 5%. If the progress object is connected to a progress bar, the bar would visibly jump backward from 50% to 5%, which may not be desirable.

To update [`totalUnitCount`](progress/totalunitcount.md) in a thread-safe manner, use the [`addBarrierBlock(_:)`](operationqueue/addbarrierblock(_:).md) method. This method ensures that the operation queue completes the operations in the queue, preventing an inadvertent backward jump in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/progress)*