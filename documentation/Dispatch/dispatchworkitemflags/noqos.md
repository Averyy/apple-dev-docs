# noQoS

**Framework**: Dispatch  
**Kind**: property  
**Role**: Type Property

Execute the work item without assigning a quality-of-service class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static let noQoS: DispatchWorkItemFlags
```

## Discussion

This flag takes priority over the [`assignCurrentContext`](./assigncurrentcontext.md) flag.

## See Also

### Work Item Flags
- [static let assignCurrentContext: DispatchWorkItemFlags](./assigncurrentcontext.md)
  Set the attributes of the work item to match the attributes of the current execution context.
- [static let barrier: DispatchWorkItemFlags](./barrier.md)
  Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [static let detached: DispatchWorkItemFlags](./detached.md)
  Disassociate the work item’s attributes from the current execution context.
- [static let enforceQoS: DispatchWorkItemFlags](./enforceqos.md)
  Prefer the quality-of-service class associated with the block.
- [static let inheritQoS: DispatchWorkItemFlags](./inheritqos.md)
  Prefer the quality-of-service class associated with the current execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/noqos)*