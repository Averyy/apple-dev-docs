# DispatchQueue.SchedulerOptions

**Framework**: Dispatch  
**Kind**: struct

A set of options that affect the operation of the dispatch queue scheduler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
struct SchedulerOptions
```

## Topics

### Creating Dispatch Queue Scheduler Options
- [init(qos: DispatchQoS, flags: DispatchWorkItemFlags, group: DispatchGroup?)](dispatchqueue/scheduleroptions/init(qos:flags:group:).md)
  Creates a dispatch queue scheduler options instance with the given options.
### Inspecting Scheduler Options
- [var qos: DispatchQoS](dispatchqueue/scheduleroptions/qos.md)
  The dispatch queue quality of service.
- [var flags: DispatchWorkItemFlags](dispatchqueue/scheduleroptions/flags.md)
  The dispatch queue work item flags.
- [var group: DispatchGroup?](dispatchqueue/scheduleroptions/group.md)
  The dispatch group, if any, to use when performing actions.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DispatchQueue.SchedulerTimeType](dispatchqueue/schedulertimetype.md)
  The scheduler time type used by the dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/scheduleroptions)*