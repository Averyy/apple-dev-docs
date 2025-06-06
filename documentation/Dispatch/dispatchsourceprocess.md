# DispatchSourceProcess

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that monitors an external process for events.

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
protocol DispatchSourceProcess : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeProcessSource(identifier:eventMask:queue:)`](dispatchsource/makeprocesssource(identifier:eventmask:queue:).md) method to create an object that adopts this protocol.

## Topics

### Getting the Process ID
- [var handle: pid_t](dispatchsourceprocess/handle.md)
  The process identifier of the process being monitored by the dispatch source.
### Getting the Event Data
- [var data: DispatchSource.ProcessEvent](dispatchsourceprocess/data.md)
  Data associated with the last process-related event.
- [var mask: DispatchSource.ProcessEvent](dispatchsourceprocess/mask.md)
  The process events being monitored by the dispatch source.

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class func makeProcessSource(identifier: pid_t, eventMask: DispatchSource.ProcessEvent, queue: DispatchQueue?) -> any DispatchSourceProcess](dispatchsource/makeprocesssource(identifier:eventmask:queue:).md)
  Creates a new dispatch source object for monitoring the specified process.
- [DispatchSource.ProcessEvent](dispatchsource/processevent.md)
  Events related to a process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprocess)*