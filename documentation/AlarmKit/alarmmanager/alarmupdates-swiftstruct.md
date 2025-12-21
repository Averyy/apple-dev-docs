# AlarmManager.AlarmUpdates

**Framework**: AlarmKit  
**Kind**: struct

An async sequence that publishes whenever an alarm changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

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