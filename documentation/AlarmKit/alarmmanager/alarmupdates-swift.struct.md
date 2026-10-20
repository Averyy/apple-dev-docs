# AlarmManager.AlarmUpdates

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An async sequence that publishes whenever an alarm changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct AlarmUpdates
```

## Topics

### Creating an iterator
- [AlarmManager.AlarmUpdates.Iterator](./alarmupdates-swift.struct/iterator.md)
  A nested type that iterates over the elements of this sequence.
- [func makeAsyncIterator() -> AlarmManager.AlarmUpdates.Iterator](./alarmupdates-swift.struct/makeasynciterator%28%29.md)
  Returns an async iterator over the elements of this sequence.
- [AlarmManager.AlarmUpdates.Element](./alarmupdates-swift.struct/element.md)
  A type representing the sequence’s elements.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Updating an alarm
- [var alarmUpdates: some AsyncSequence<Array<Alarm>, Never>](./alarmupdates-swift.property.md)
  An asynchronous sequence that emits events when the set of alarms changes.
- [var alarms: [Alarm]](./alarms.md)
  Fetches all alarms from the daemon that belong to the current client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmupdates-swift.struct)*