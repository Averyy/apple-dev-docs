# DispatchWorkItemFlags

**Framework**: Dispatch  
**Kind**: struct

A set of behaviors for a work item, such as its quality-of-service class and whether to create a barrier or spawn a new detached thread.

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
struct DispatchWorkItemFlags
```

## Topics

### Work Item Flags
- [static let assignCurrentContext: DispatchWorkItemFlags](dispatchworkitemflags/assigncurrentcontext.md)
  Set the attributes of the work item to match the attributes of the current execution context.
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

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [init(qos: DispatchQoS, flags: DispatchWorkItemFlags, block: () -> Void)](dispatchworkitem/init(qos:flags:block:).md)
  Creates a new dispatch work item from an existing block and assigns it the specified quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags)*