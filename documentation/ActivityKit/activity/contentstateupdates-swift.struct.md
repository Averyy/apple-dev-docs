# Activity.ContentStateUpdates

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

A structure that offers functionality to observe changes to the dynamic content of a Live Activity.

**Availability**:
- iOS 16.1+ - Deprecated in 16.2
- iPadOS 16.1+ - Deprecated in 16.2

> **Deprecated**: Use `ContentUpdates` instead

## Declaration

```swift
struct ContentStateUpdates
```

Available when `Attributes` conforms to `ActivityAttributes`.

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> Activity<Attributes>.ContentStateUpdates.Iterator](./contentstateupdates-swift.struct/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.ContentStateUpdates.Iterator](./contentstateupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.ContentStateUpdates.Element](./contentstateupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Deprecated
- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](./request%28attributes,contentstate,pushtype%29.md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](./update%28using%29.md)
  Updates the dynamic content of the Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](./update%28using,alertconfiguration%29.md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](./end%28using,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](./contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](./contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct)*