# AlarmManager.AlarmAuthorizationStateUpdates

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct AlarmAuthorizationStateUpdates
```

## Topics

### Iterating an update
- [AlarmManager.AlarmAuthorizationStateUpdates.Iterator](./alarmauthorizationstateupdates/iterator.md)
  A nested type that iterates over the elements of this sequence.
- [func makeAsyncIterator() -> AlarmManager.AlarmAuthorizationStateUpdates.Iterator](./alarmauthorizationstateupdates/makeasynciterator%28%29.md)
  Returns an asynchronous iterator over the elements of this sequence.
- [AlarmManager.AlarmAuthorizationStateUpdates.Element](./alarmauthorizationstateupdates/element.md)
  A type representing the sequence’s elements.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Checking authorization status
- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](./authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [AlarmManager.AuthorizationState](./authorizationstate-swift.enum.md)
  An enumeration describing all authorization states for the client process.
- [var authorizationState: AlarmManager.AuthorizationState](./authorizationstate-swift.property.md)
  Returns the current authorization state for this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmauthorizationstateupdates)*