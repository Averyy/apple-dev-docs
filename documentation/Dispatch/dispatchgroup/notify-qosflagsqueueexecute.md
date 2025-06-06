# notify(qos:flags:queue:execute:)

**Framework**: Dispatch  
**Kind**: method

Schedules the submission of a block with the specified attributes to a queue when all tasks in the current group have finished executing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func notify(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], queue: DispatchQueue, execute work: @escaping () -> Void)
```

#### Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately. When the notification block is submitted, the group is empty.

## Parameters

- `qos`: The quality of service class for the work to be performed.
- `flags`: For possible values, see  .
- `queue`: The queue to which the supplied block is submitted when the group completes.
- `work`: The work to be performed on the dispatch queue when the group is completed.

## See Also

- [func notify(queue: DispatchQueue, work: DispatchWorkItem)](dispatchgroup/notify(queue:work:).md)
  Schedules the submission of a block to a queue when all tasks in the current group have finished executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/notify(qos:flags:queue:execute:))*