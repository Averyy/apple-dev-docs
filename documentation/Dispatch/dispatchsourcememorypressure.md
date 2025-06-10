# DispatchSourceMemoryPressure

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that monitors the system for changes in the memory pressure condition.

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
protocol DispatchSourceMemoryPressure : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeMemoryPressureSource(eventMask:queue:)`](dispatchsource/makememorypressuresource(eventmask:queue:).md) method to create an object that adopts this protocol.

## Topics

### Getting the Event Data
- [var data: DispatchSource.MemoryPressureEvent](dispatchsourcememorypressure/data.md)
- [var mask: DispatchSource.MemoryPressureEvent](dispatchsourcememorypressure/mask.md)

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class func makeMemoryPressureSource(eventMask: DispatchSource.MemoryPressureEvent, queue: DispatchQueue?) -> any DispatchSourceMemoryPressure](dispatchsource/makememorypressuresource(eventmask:queue:).md)
  Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent.md)
  Memory pressure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcememorypressure)*