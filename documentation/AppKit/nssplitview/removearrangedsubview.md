# removeArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method

Removes a view as an arranged split pane.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func removeArrangedSubview(_ view: NSView)
```

#### Discussion

If the value of [`arrangesAllSubviews`](nssplitview/arrangesallsubviews.md) is [`false`](https://developer.apple.com/documentation/Swift/false), calling this method doesn’t remove the view as a subview; it remains in the split view’s [`subviews`](nsview/subviews.md) array.

If you remove a view as a subview (either by calling [`removeFromSuperview()`](nsview/removefromsuperview().md) or removing it from the split view’s [`subviews`](nsview/subviews.md) array), the system automatically removes the view as an arranged subview.

## See Also

- [var arrangesAllSubviews: Bool](nssplitview/arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](nssplitview/arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](nssplitview/addarrangedsubview(_:).md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](nssplitview/insertarrangedsubview(_:at:).md)
  Adds a view as an arranged split pane at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/removearrangedsubview(_:))*