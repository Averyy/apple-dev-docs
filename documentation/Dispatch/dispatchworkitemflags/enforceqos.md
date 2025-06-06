# enforceQoS

**Framework**: Dispatch  
**Kind**: property

Prefer the quality-of-service class associated with the block.

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
static let enforceQoS: DispatchWorkItemFlags
```

#### Discussion

This flag prioritizes the block’s quality-of-service class over the one associated with the current execution context, as long as doing so does not lower the quality of service.

## See Also

- [static let assignCurrentContext: DispatchWorkItemFlags](dispatchworkitemflags/assigncurrentcontext.md)
  Set the attributes of the work item to match the attributes of the current execution context.
- [static let barrier: DispatchWorkItemFlags](dispatchworkitemflags/barrier.md)
  Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [static let detached: DispatchWorkItemFlags](dispatchworkitemflags/detached.md)
  Disassociate the work item’s attributes from the current execution context.
- [static let inheritQoS: DispatchWorkItemFlags](dispatchworkitemflags/inheritqos.md)
  Prefer the quality-of-service class associated with the current execution context.
- [static let noQoS: DispatchWorkItemFlags](dispatchworkitemflags/noqos.md)
  Execute the work item without assigning a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/enforceqos)*