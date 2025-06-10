# AlarmManager.AlarmUpdates

**Framework**: AlarmKit  
**Kind**: struct

An async sequence that publishes whenever an alarm changes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct AlarmUpdates
```

## Topics

### Creating an iterator
- [AlarmManager.AlarmUpdates.Iterator](alarmmanager/alarmupdates-swift.struct/iterator.md)
  A nested type that iterates over the elements of this sequence.
- [func makeAsyncIterator() -> AlarmManager.AlarmUpdates.Iterator](alarmmanager/alarmupdates-swift.struct/makeasynciterator.md)
  Returns an asynchronous iterator over the elements of this sequence.
- [AlarmManager.AlarmUpdates.Element](alarmmanager/alarmupdates-swift.struct/element.md)
  A type representing the sequence’s elements.
### Type Aliases
- [AlarmManager.AlarmUpdates.AsyncIterator](alarmmanager/alarmupdates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](alarmmanager/alarmupdates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var alarmUpdates: some AsyncSequence<Array<Alarm>, Never>](alarmmanager/alarmupdates-swift.property.md)
  An asynchronous sequence that emits events when the set of alarms changes.
- [var alarms: [Alarm]](alarmmanager/alarms.md)
  Fetches all alarms from the daemon that belong to the current client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmupdates-swift.struct)*