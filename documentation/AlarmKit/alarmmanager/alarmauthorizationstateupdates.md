# AlarmManager.AlarmAuthorizationStateUpdates

**Framework**: AlarmKit  
**Kind**: struct

An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct AlarmAuthorizationStateUpdates
```

## Topics

### Iterating an update
- [AlarmManager.AlarmAuthorizationStateUpdates.Iterator](alarmmanager/alarmauthorizationstateupdates/iterator.md)
  A nested type that iterates over the elements of this sequence.
- [func makeAsyncIterator() -> AlarmManager.AlarmAuthorizationStateUpdates.Iterator](alarmmanager/alarmauthorizationstateupdates/makeasynciterator.md)
  Returns an asynchronous iterator over the elements of this sequence.
- [AlarmManager.AlarmAuthorizationStateUpdates.Element](alarmmanager/alarmauthorizationstateupdates/element.md)
  A type representing the sequence’s elements.
### Type Aliases
- [AlarmManager.AlarmAuthorizationStateUpdates.AsyncIterator](alarmmanager/alarmauthorizationstateupdates/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](alarmmanager/alarmauthorizationstateupdates/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](alarmmanager/authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [AlarmManager.AuthorizationState](alarmmanager/authorizationstate-swift.enum.md)
  An enumeration describing all authorization states for the client process.
- [var authorizationState: AlarmManager.AuthorizationState](alarmmanager/authorizationstate-swift.property.md)
  Returns the current authorization state for this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmauthorizationstateupdates)*