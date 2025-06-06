# EKEntityMask

**Framework**: EventKit  
**Kind**: struct

A bitmask of `EKEntityType` for specifying multiple entities at once.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct EKEntityMask
```

## Topics

### Initializers
- [init(rawValue: UInt)](ekentitymask/init(rawvalue:).md)
  Creates an entity mask with the specified raw value.
### Constants
- [static var event: EKEntityMask](ekentitymask/event.md)
  Represents an event.
- [static var reminder: EKEntityMask](ekentitymask/reminder.md)
  Represents a reminder.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekentitymask)*