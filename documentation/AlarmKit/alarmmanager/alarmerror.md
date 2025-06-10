# AlarmManager.AlarmError

**Framework**: AlarmKit  
**Kind**: enum

An error that occurs when trying to schedule a timer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum AlarmError
```

## Topics

### Checking for alarm limit
- [AlarmManager.AlarmError.maximumLimitReached](alarmmanager/alarmerror/maximumlimitreached.md)
  A maximum number of alarms is already scheduled.
### Operators
- [static func == (AlarmManager.AlarmError, AlarmManager.AlarmError) -> Bool](alarmmanager/alarmerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarmmanager/alarmerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](alarmmanager/alarmerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarmmanager/alarmerror/equatable-implementations.md)
- [Error Implementations](alarmmanager/alarmerror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmerror)*