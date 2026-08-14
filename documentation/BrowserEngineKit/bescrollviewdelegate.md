# BEScrollViewDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol for scroll view delegates to handle scroll updates and DOM nesting.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
protocol BEScrollViewDelegate : UIScrollViewDelegate
```

## Topics

### Nesting sibling scroll views
- [func parentScrollView(for: BEScrollView) -> BEScrollView?](bescrollviewdelegate/parentscrollview(for:).md)
  Returns the scroll view that acts as the DOM container of the given scroll view.
### Handling scroll events
- [func scrollView(BEScrollView, handle: BEScrollViewScrollUpdate, completion: (Bool) -> Void)](bescrollviewdelegate/scrollview(_:handle:completion:).md)
  Handles a scroll update before the scroll view reacts to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UIScrollViewDelegate](../uikit/uiscrollviewdelegate.md)

## See Also

- [class BEScrollView](bescrollview.md)
  A scroll view that works with its delegate to handle nesting and customize scroll interactions.
- [class BEScrollViewScrollUpdate](bescrollviewscrollupdate.md)
  An object that describes a change in a scroll view’s scroll state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewdelegate)*