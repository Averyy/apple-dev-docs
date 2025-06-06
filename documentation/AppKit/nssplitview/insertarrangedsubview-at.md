# insertArrangedSubview(_:at:)

**Framework**: AppKit  
**Kind**: method

Adds a view as an arranged split pane at the specified index.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func insertArrangedSubview(_ view: NSView, at index: Int)
```

#### Discussion

If the view is already an arranged view, calling this method moves the view to the specified index in the [`arrangedSubviews`](nssplitview/arrangedsubviews.md) array. This change doesn’t affect the view’s index in the split view’s [`subviews`](nsview/subviews.md) array.

If the view isn’t a subview of the split view, calling this method adds it to the split view’s [`subviews`](nsview/subviews.md) array.

## See Also

- [var arrangesAllSubviews: Bool](nssplitview/arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](nssplitview/arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](nssplitview/addarrangedsubview(_:).md)
  Adds a view as an arranged split pane.
- [func removeArrangedSubview(NSView)](nssplitview/removearrangedsubview(_:).md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/insertarrangedsubview(_:at:))*