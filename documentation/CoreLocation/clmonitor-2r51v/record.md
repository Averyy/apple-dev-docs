# CLMonitor.Record

**Framework**: Core Location  
**Kind**: struct

A structure that represents a condition and its associated event information that the framework is monitoring.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Record
```

#### Overview

The `CLMonitor.Record` contains a condition and most recent event that affects it.

## Topics

### Record characteristics
- [let condition: any CLCondition](clmonitor-2r51v/record/condition.md)
  The condition that the framework is monitoring for.
- [let lastEvent: CLMonitor.Event](clmonitor-2r51v/record/lastevent.md)
  The most recent event the monitor records.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [CLMonitor.Event](clmonitor-2r51v/event.md)
  An event object that the framework passes to the events sequence in the monitor.
- [CLMonitor.Events](clmonitor-2r51v/events-swift.struct.md)
  A type that represents an asynchronous sequence of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/record)*