# EKEntityType

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The type of entities allowed for a source.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKEntityType
```

```c
enum EKEntityType : NSUInteger;
```

## Topics

### Specifying Multiple Entities
- [struct EKEntityMask](./ekentitymask.md)
  A bitmask of `EKEntityType` for specifying multiple entities at once.
### Constants
- [EKEntityType.event](./ekentitytype/event.md)
  Represents an event.
- [EKEntityType.reminder](./ekentitytype/reminder.md)
  Represents a reminder.
### Initializers
- [init?(rawValue: UInt)](./ekentitytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekentitytype)*