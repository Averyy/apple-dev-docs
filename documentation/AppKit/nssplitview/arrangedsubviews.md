# arrangedSubviews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of views that the split view arranges as its split panes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var arrangedSubviews: [NSView] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSView *> * arrangedSubviews;
```

#### Discussion

This array contains a subset of the views in the split view’s [`subviews`](../nsview/subviews.md) property. The views in this array may appear in a different order than in the [`subviews`](../nsview/subviews.md) array.

If the value of [`arrangesAllSubviews`](./arrangesallsubviews.md) is [`true`](../../Swift/true.md), this array is identical to the [`subviews`](../nsview/subviews.md) array.

## See Also

### Arranging Subviews
- [var arrangesAllSubviews: Bool](./arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/arrangedsubviews)*