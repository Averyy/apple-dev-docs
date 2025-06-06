# async(group:execute:)

**Framework**: Dispatch  
**Kind**: method

Schedules a work item asynchronously for execution and associates it with the specified dispatch group.

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
func async(group: DispatchGroup, execute workItem: DispatchWorkItem)
```

#### Discussion

This method adds the work item to the group before scheduling it on the current queue.

## Parameters

- `group`: The dispatch group to associate with the work item. This parameter cannot be  .
- `workItem`: The work item containing the task to execute. For information on how to create this work item, see  .

## See Also

- [func async(group: DispatchGroup?, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](dispatchqueue/async(group:qos:flags:execute:).md)
  Schedules a block asynchronously for execution and optionally associates it with a dispatch group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/async(group:execute:))*