# arrangesAllSubviews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the split view arranges all of its subviews as split panes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var arrangesAllSubviews: Bool { get set }
```

```objc
@property BOOL arrangesAllSubviews;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the split view arranges all of its subviews automatically. The [`arrangedSubviews`](./arrangedsubviews.md) array is identical to the split view’s [`subviews`](../nsview/subviews.md) array, so any change to [`subviews`](../nsview/subviews.md) reflects in the [`arrangedSubviews`](./arrangedsubviews.md) array. The default value of this property is [`true`](../../Swift/true.md).

If the value of this property is [`false`](../../Swift/false.md), you must explicitly add a view as an arranged subview to arrange it as a split pane. You add an arranged subview using [`addArrangedSubview(_:)`](./addarrangedsubview%28_%29.md).

When you change the value of this property from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md), all existing subviews stay as arranged subviews in [`arrangedSubviews`](./arrangedsubviews.md). When you change the value of this property from [`false`](../../Swift/false.md) to [`true`](../../Swift/true.md), all existing subviews become arranged subviews, and the value of the [`subviews`](../nsview/subviews.md) array becomes the [`arrangedSubviews`](./arrangedsubviews.md) array.

## See Also

### Arranging Subviews
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/arrangesallsubviews)*