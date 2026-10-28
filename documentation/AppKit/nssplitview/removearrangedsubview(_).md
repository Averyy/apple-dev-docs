# removeArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a view as an arranged split pane.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func removeArrangedSubview(_ view: NSView)
```

```objc
- (void) removeArrangedSubview:(NSView *) view;
```

## Discussion

If the value of [`arrangesAllSubviews`](./arrangesallsubviews.md) is [`false`](../../Swift/false.md), calling this method doesn’t remove the view as a subview; it remains in the split view’s [`subviews`](../nsview/subviews.md) array.

If you remove a view as a subview (either by calling [`removeFromSuperview()`](../nsview/removefromsuperview%28%29.md) or removing it from the split view’s [`subviews`](../nsview/subviews.md) array), the system automatically removes the view as an arranged subview.

## See Also

### Arranging Subviews
- [var arrangesAllSubviews: Bool](./arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds a view as an arranged split pane at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/removearrangedsubview(_:))*