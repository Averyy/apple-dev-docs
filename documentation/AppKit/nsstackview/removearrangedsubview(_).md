# removeArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the provided view from the stack’s array of arranged subviews.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func removeArrangedSubview(_ view: NSView)
```

```objc
- (void) removeArrangedSubview:(NSView *) view;
```

#### Discussion

This method removes the provided view from the stack’s [`arrangedSubviews`](./arrangedsubviews.md) array. After calling this method, the stack view no longer manages the view’s position and size. However, this method does not remove the provided view from the stack’s [`subviews`](../nsview/subviews.md) array; therefore, the view still appears in the view hierarchy.

To prevent the view from appearing on screen after calling this method, explicitly call the view’s [`removeFromSuperview()`](../nsview/removefromsuperview%28%29.md) method, or set its [`isHidden`](../nsview/ishidden.md) property to [`true`](../../Swift/true.md).

## Parameters

- `view`: The view to be removed from the array of views arranged by the stack.

## See Also

### Managing the Arranged Subviews
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds the specified view to the end of the arranged subviews list.
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views arranged by the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/removearrangedsubview(_:))*