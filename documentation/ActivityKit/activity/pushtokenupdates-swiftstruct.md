# Activity.PushTokenUpdates

**Framework**: ActivityKit  
**Kind**: struct

A structure that offers functionality to observe changes to the push token of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct PushTokenUpdates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.PushTokenUpdates.Iterator](activity/pushtokenupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.PushTokenUpdates.Iterator](activity/pushtokenupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.PushTokenUpdates.Element](activity/pushtokenupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var pushToken: Data?](activity/pushtoken.md)
  The token you use to send ActivityKit push notifications to a Live Activity.
- [var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtokenupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [static var pushToStartToken: Data?](activity/pushtostarttoken.md)
  The token you use to start a Live Activity with an ActivityKit push notification.
- [static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtostarttokenupdates.md)
  An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.struct)*