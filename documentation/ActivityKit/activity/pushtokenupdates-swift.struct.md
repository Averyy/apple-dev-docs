# Activity.PushTokenUpdates

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

A structure that offers functionality to observe changes to the push token of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct PushTokenUpdates
```

Available when `Attributes` conforms to `ActivityAttributes`.

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.PushTokenUpdates.Iterator](./pushtokenupdates-swift.struct/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.PushTokenUpdates.Iterator](./pushtokenupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.PushTokenUpdates.Element](./pushtokenupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Using ActivityKit push notifications
- [var pushToken: Data?](./pushtoken.md)
  The token you use to send ActivityKit push notifications to a Live Activity.
- [var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates](./pushtokenupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [static var pushToStartToken: Data?](./pushtostarttoken.md)
  The token you use to start a Live Activity with an ActivityKit push notification.
- [static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates](./pushtostarttokenupdates.md)
  An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.struct)*