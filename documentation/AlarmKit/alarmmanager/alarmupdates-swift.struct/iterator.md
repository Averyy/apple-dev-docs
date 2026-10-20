# AlarmManager.AlarmUpdates.Iterator

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

A nested type that iterates over the elements of this sequence.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Interating a function
- [func next() async -> AlarmManager.AlarmUpdates.Element?](./iterator/next%28%29.md)
  Returns the next element in the sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> AlarmManager.AlarmUpdates.Iterator](./makeasynciterator%28%29.md)
  Returns an async iterator over the elements of this sequence.
- [AlarmManager.AlarmUpdates.Element](./element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmupdates-swift.struct/iterator)*