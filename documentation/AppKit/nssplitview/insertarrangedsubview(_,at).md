# insertArrangedSubview(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a view as an arranged split pane at the specified index.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func insertArrangedSubview(_ view: NSView, at index: Int)
```

```objc
- (void) insertArrangedSubview:(NSView *) view atIndex:(NSInteger) index;
```

## Discussion

If the view is already an arranged view, calling this method moves the view to the specified index in the [`arrangedSubviews`](./arrangedsubviews.md) array. This change doesn’t affect the view’s index in the split view’s [`subviews`](../nsview/subviews.md) array.

If the view isn’t a subview of the split view, calling this method adds it to the split view’s [`subviews`](../nsview/subviews.md) array.

## See Also

### Arranging Subviews
- [var arrangesAllSubviews: Bool](./arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds a view as an arranged split pane.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/insertarrangedsubview(_:at:))*