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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekentitymask)*