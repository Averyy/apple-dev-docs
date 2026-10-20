# Activity.ActivityStateUpdates

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

A structure that offers functionality to observe state changes of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ActivityStateUpdates
```

Available when `Attributes` conforms to `ActivityAttributes`.

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.ActivityStateUpdates.Iterator](./activitystateupdates-swift.struct/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.ActivityStateUpdates.Iterator](./activitystateupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.ActivityStateUpdates.Element](./activitystateupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Observing the Live Activity life cycle
- [var activityState: ActivityState](./activitystate.md)
  The current state of a Live Activity in its life cycle.
- [enum ActivityState](../activitystate.md)
  The enum that describes the state of a Live Activity in its life cycle.
- [var activityStateUpdates: Activity<Attributes>.ActivityStateUpdates](./activitystateupdates-swift.property.md)
  An asynchronous sequence you use to observe activity state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.struct)*