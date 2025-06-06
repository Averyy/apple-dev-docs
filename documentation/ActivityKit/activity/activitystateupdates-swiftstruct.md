# Activity.ActivityStateUpdates

**Framework**: ActivityKit  
**Kind**: struct

A structure that offers functionality to observe state changes of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ActivityStateUpdates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.ActivityStateUpdates.Iterator](activity/activitystateupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.ActivityStateUpdates.Iterator](activity/activitystateupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.ActivityStateUpdates.Element](activity/activitystateupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.
### Type Aliases
- [Activity.ActivityStateUpdates.AsyncIterator](activity/activitystateupdates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](activity/activitystateupdates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var activityState: ActivityState](activity/activitystate.md)
  The current state of a Live Activity in its life cycle.
- [enum ActivityState](activitystate.md)
  The enum that describes the state of a Live Activity in its life cycle.
- [var activityStateUpdates: Activity<Attributes>.ActivityStateUpdates](activity/activitystateupdates-swift.property.md)
  An asynchronous sequence you use to observe activity state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.struct)*