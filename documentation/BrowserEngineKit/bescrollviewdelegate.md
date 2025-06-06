# BEScrollViewDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol

The protocol that browser scroll view delegates conform to.

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
  Indicates that a sibling scroll view in the view hierarchy acts as the scroll view’s container in the Document Object Model (DOM).
### Handling scroll events
- [func scrollView(BEScrollView, handle: BEScrollViewScrollUpdate, completion: (Bool) -> Void)](bescrollviewdelegate/scrollview(_:handle:completion:).md)
  Handles a scroll update, optionally stopping the scroll view from reacting.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIScrollViewDelegate](../UIKit/UIScrollViewDelegate.md)

## See Also

- [class BEScrollView](bescrollview.md)
  A scroll view that works with its delegate to handle nesting, and customize scroll interactions.
- [class BEScrollViewScrollUpdate](bescrollviewscrollupdate.md)
  An object that represents a change in a scroll view’s scroll state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewdelegate)*