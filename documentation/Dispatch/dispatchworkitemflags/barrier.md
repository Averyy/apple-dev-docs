# barrier

**Framework**: Dispatch  
**Kind**: property

Cause the work item to act as a barrier block when submitted to a concurrent queue.

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
static let barrier: DispatchWorkItemFlags
```

#### Discussion

When submitted to a concurrent queue, a work item with this flag acts as a barrier. Work items submitted prior to the barrier execute to completion, at which point the barrier work item executes. Once the barrier work item finishes, the queue returns to scheduling work items that were submitted after the barrier.

## See Also

- [static let assignCurrentContext: DispatchWorkItemFlags](dispatchworkitemflags/assigncurrentcontext.md)
  Set the attributes of the work item to match the attributes of the current execution context.
- [static let detached: DispatchWorkItemFlags](dispatchworkitemflags/detached.md)
  Disassociate the work item’s attributes from the current execution context.
- [static let enforceQoS: DispatchWorkItemFlags](dispatchworkitemflags/enforceqos.md)
  Prefer the quality-of-service class associated with the block.
- [static let inheritQoS: DispatchWorkItemFlags](dispatchworkitemflags/inheritqos.md)
  Prefer the quality-of-service class associated with the current execution context.
- [static let noQoS: DispatchWorkItemFlags](dispatchworkitemflags/noqos.md)
  Execute the work item without assigning a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/barrier)*