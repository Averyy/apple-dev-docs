# addArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method

Adds a view as an arranged split pane.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func addArrangedSubview(_ view: NSView)
```

#### Discussion

If the view isn’t a subview of the split view, calling this method adds it to the split view’s [`subviews`](nsview/subviews.md) array.

## See Also

- [var arrangesAllSubviews: Bool](nssplitview/arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](nssplitview/arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func insertArrangedSubview(NSView, at: Int)](nssplitview/insertarrangedsubview(_:at:).md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](nssplitview/removearrangedsubview(_:).md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/addarrangedsubview(_:))*