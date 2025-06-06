# detached

**Framework**: Dispatch  
**Kind**: property

Disassociate the work item’s attributes from the current execution context.

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
static let detached: DispatchWorkItemFlags
```

#### Discussion

When this flag is set, the system does not apply attributes from the current execution context to the work item.

## See Also

- [static let assignCurrentContext: DispatchWorkItemFlags](dispatchworkitemflags/assigncurrentcontext.md)
  Set the attributes of the work item to match the attributes of the current execution context.
- [static let barrier: DispatchWorkItemFlags](dispatchworkitemflags/barrier.md)
  Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [static let enforceQoS: DispatchWorkItemFlags](dispatchworkitemflags/enforceqos.md)
  Prefer the quality-of-service class associated with the block.
- [static let inheritQoS: DispatchWorkItemFlags](dispatchworkitemflags/inheritqos.md)
  Prefer the quality-of-service class associated with the current execution context.
- [static let noQoS: DispatchWorkItemFlags](dispatchworkitemflags/noqos.md)
  Execute the work item without assigning a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/detached)*