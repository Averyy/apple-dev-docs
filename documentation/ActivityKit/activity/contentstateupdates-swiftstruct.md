# Activity.ContentStateUpdates

**Framework**: ActivityKit  
**Kind**: struct

A structure that offers functionality to observe changes to the dynamic content of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ContentStateUpdates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.ContentStateUpdates.Iterator](activity/contentstateupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.ContentStateUpdates.Iterator](activity/contentstateupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.ContentStateUpdates.Element](activity/contentstateupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.
### Type Aliases
- [Activity.ContentStateUpdates.AsyncIterator](activity/contentstateupdates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](activity/contentstateupdates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:contentstate:pushtype:).md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](activity/update(using:).md)
  Updates the dynamic content of the Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](activity/update(using:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](activity/end(using:dismissalpolicy:).md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](activity/contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](activity/contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct)*