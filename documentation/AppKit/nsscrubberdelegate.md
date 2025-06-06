# NSScrubberDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a scrubber delegate implements to respond to user interactions.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSScrubberDelegate : NSObjectProtocol
```

## Topics

### Handling item selection and highlighting
- [func scrubber(NSScrubber, didSelectItemAt: Int)](nsscrubberdelegate/scrubber(_:didselectitemat:).md)
  Tells the delegate that the item at the specified index was selected.
- [func scrubber(NSScrubber, didHighlightItemAt: Int)](nsscrubberdelegate/scrubber(_:didhighlightitemat:).md)
  Tells the delegate that the item at the specified index was highlighted.
### Handling scrubber scrolling
- [func scrubber(NSScrubber, didChangeVisibleRange: NSRange)](nsscrubberdelegate/scrubber(_:didchangevisiblerange:).md)
  Tells the delegate that the range of items currently visible in the scrubber has changed.
### Tracking user interaction
- [func didBeginInteracting(with: NSScrubber)](nsscrubberdelegate/didbegininteracting(with:).md)
  Tells the delegate that the user is panning or scrolling the scrubber.
- [func didFinishInteracting(with: NSScrubber)](nsscrubberdelegate/didfinishinteracting(with:).md)
  Tells the delegate that a pan or scroll interaction with the scrubber has ended.
- [func didCancelInteracting(with: NSScrubber)](nsscrubberdelegate/didcancelinteracting(with:).md)
  Tells the delegate that a user interaction with the scrubber has been canceled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSScrubberFlowLayoutDelegate](nsscrubberflowlayoutdelegate.md)

## See Also

- [class NSScrubber](nsscrubber.md)
  A customizable item picker control for the Touch Bar.
- [protocol NSScrubberDataSource](nsscrubberdatasource.md)
  A set of methods that a scrubber data source object implements to provide items to the scrubber from an associated data collection in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdelegate)*