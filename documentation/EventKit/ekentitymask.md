# EKEntityMask

**Framework**: EventKit  
**Kind**: struct  
**Role**: Structure

A bitmask of `EKEntityType` for specifying multiple entities at once.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
struct EKEntityMask
```

```c
enum EKEntityMask : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./ekentitymask/init%28rawvalue%29.md)
  Creates an entity mask with the specified raw value.
### Constants
- [static var event: EKEntityMask](./ekentitymask/event.md)
  Represents an event.
- [static var reminder: EKEntityMask](./ekentitymask/reminder.md)
  Represents a reminder.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekentitymask)*