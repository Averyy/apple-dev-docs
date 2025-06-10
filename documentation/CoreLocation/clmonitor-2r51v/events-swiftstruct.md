# CLMonitor.Events

**Framework**: Core Location  
**Kind**: struct

A type that represents an asynchronous sequence of events.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Events
```

#### Overview

Use this structure to access and iterate over the events the framework delivers.

## Topics

### Utility methods
- [CLMonitor.Events.Iterator](clmonitor-2r51v/events-swift.struct/iterator.md)
  The type that allows iteration over the elements of the sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CLMonitor.Event](clmonitor-2r51v/event.md)
  An event object that the framework passes to the events sequence in the monitor.
- [CLMonitor.Record](clmonitor-2r51v/record.md)
  A structure that represents a condition and its associated event information that the framework is monitoring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/events-swift.struct)*