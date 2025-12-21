# removeArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method

Removes the provided view from the stack’s array of arranged subviews.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func removeArrangedSubview(_ view: NSView)
```

#### Discussion

This method removes the provided view from the stack’s [`arrangedSubviews`](nsstackview/arrangedsubviews.md) array. After calling this method, the stack view no longer manages the view’s position and size. However, this method does not remove the provided view from the stack’s [`subviews`](nsview/subviews.md) array; therefore, the view still appears in the view hierarchy.

To prevent the view from appearing on screen after calling this method, explicitly call the view’s [`removeFromSuperview()`](nsview/removefromsuperview().md) method, or set its [`isHidden`](nsview/ishidden.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `view`: The view to be removed from the array of views arranged by the stack.

## See Also

- [func addArrangedSubview(NSView)](nsstackview/addarrangedsubview(_:).md)
  Adds the specified view to the end of the arranged subviews list.
- [func insertArrangedSubview(NSView, at: Int)](nsstackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [var arrangedSubviews: [NSView]](nsstackview/arrangedsubviews.md)
  The array of views arranged by the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/removearrangedsubview(_:))*