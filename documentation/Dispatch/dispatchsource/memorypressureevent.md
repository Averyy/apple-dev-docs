# DispatchSource.MemoryPressureEvent

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

Memory pressure events.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct MemoryPressureEvent
```

## Topics

### Memory Pressure Event Flags
- [static let all: DispatchSource.MemoryPressureEvent](./memorypressureevent/all.md)
  All memory pressure events.
- [static let normal: DispatchSource.MemoryPressureEvent](./memorypressureevent/normal.md)
  An event indicating that the system memory pressure condition changed to normal.
- [static let warning: DispatchSource.MemoryPressureEvent](./memorypressureevent/warning.md)
  An event indicating that the system memory pressure condition changed to warning.
- [static let critical: DispatchSource.MemoryPressureEvent](./memorypressureevent/critical.md)
  An event indicating that the system memory pressure condition changed to critical.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a Memory Pressure Source
- [class func makeMemoryPressureSource(eventMask: DispatchSource.MemoryPressureEvent, queue: DispatchQueue?) -> any DispatchSourceMemoryPressure](./makememorypressuresource%28eventmask,queue%29.md)
  Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [protocol DispatchSourceMemoryPressure](../dispatchsourcememorypressure.md)
  A dispatch source that monitors the system for changes in the memory pressure condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/memorypressureevent)*