# Activity.ActivityUpdates

**Framework**: ActivityKit  
**Kind**: struct

A structure that offers functionality to observe changes to a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ActivityUpdates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.ActivityUpdates.Iterator](activity/activityupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.ActivityUpdates.Iterator](activity/activityupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.ActivityUpdates.Element](activity/activityupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [static var activities: [Activity<Attributes>]](activity/activities.md)
  An array of your app’s current Live Activities.
- [static var activityUpdates: Activity<Attributes>.ActivityUpdates](activity/activityupdates-swift.type.property.md)
  An asynchronous sequence you use to observe changes to ongoing Live Activities and to asynchronously access a Live Activity when you start it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/activityupdates-swift.struct)*