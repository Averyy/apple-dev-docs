# addArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a view as an arranged split pane.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func addArrangedSubview(_ view: NSView)
```

```objc
- (void) addArrangedSubview:(NSView *) view;
```

## Discussion

If the view isn’t a subview of the split view, calling this method adds it to the split view’s [`subviews`](../nsview/subviews.md) array.

## See Also

### Arranging Subviews
- [var arrangesAllSubviews: Bool](./arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/addarrangedsubview(_:))*