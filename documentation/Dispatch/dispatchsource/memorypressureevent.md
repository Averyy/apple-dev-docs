# DispatchSource.MemoryPressureEvent

**Framework**: Dispatch  
**Kind**: struct

Memory pressure events.

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
struct MemoryPressureEvent
```

## Topics

### Memory Pressure Event Flags
- [static let all: DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent/all.md)
  All memory pressure events.
- [static let normal: DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent/normal.md)
  An event indicating that the system memory pressure condition changed to normal.
- [static let warning: DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent/warning.md)
  An event indicating that the system memory pressure condition changed to warning.
- [static let critical: DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent/critical.md)
  An event indicating that the system memory pressure condition changed to critical.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func makeMemoryPressureSource(eventMask: DispatchSource.MemoryPressureEvent, queue: DispatchQueue?) -> any DispatchSourceMemoryPressure](dispatchsource/makememorypressuresource(eventmask:queue:).md)
  Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [protocol DispatchSourceMemoryPressure](dispatchsourcememorypressure.md)
  A dispatch source that monitors the system for changes in the memory pressure condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/memorypressureevent)*