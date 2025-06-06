# assignCurrentContext

**Framework**: Dispatch  
**Kind**: property

Set the attributes of the work item to match the attributes of the current execution context.

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
static let assignCurrentContext: DispatchWorkItemFlags
```

#### Discussion

When this flag is set, the work item inherits attributes such as the quality-of-service class from the dispatch queue or thread responsible for executing the task.

## See Also

- [static let barrier: DispatchWorkItemFlags](dispatchworkitemflags/barrier.md)
  Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [static let detached: DispatchWorkItemFlags](dispatchworkitemflags/detached.md)
  Disassociate the work item’s attributes from the current execution context.
- [static let enforceQoS: DispatchWorkItemFlags](dispatchworkitemflags/enforceqos.md)
  Prefer the quality-of-service class associated with the block.
- [static let inheritQoS: DispatchWorkItemFlags](dispatchworkitemflags/inheritqos.md)
  Prefer the quality-of-service class associated with the current execution context.
- [static let noQoS: DispatchWorkItemFlags](dispatchworkitemflags/noqos.md)
  Execute the work item without assigning a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/assigncurrentcontext)*