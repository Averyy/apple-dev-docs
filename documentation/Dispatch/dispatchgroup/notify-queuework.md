# notify(queue:work:)

**Framework**: Dispatch  
**Kind**: method

Schedules the submission of a block to a queue when all tasks in the current group have finished executing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func notify(queue: DispatchQueue, work: DispatchWorkItem)
```

#### Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately. When the notification block is submitted, the group is empty.

## Parameters

- `queue`: The queue to which the supplied block is submitted when the group completes.
- `work`: The work to be performed on the dispatch queue when the group is completed.

## See Also

- [func notify(qos: DispatchQoS, flags: DispatchWorkItemFlags, queue: DispatchQueue, execute: () -> Void)](dispatchgroup/notify(qos:flags:queue:execute:).md)
  Schedules the submission of a block with the specified attributes to a queue when all tasks in the current group have finished executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/notify(queue:work:))*