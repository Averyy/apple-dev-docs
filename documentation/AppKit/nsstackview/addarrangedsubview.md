# addArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method

Adds the specified view to the end of the arranged subviews list.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func addArrangedSubview(_ view: NSView)
```

#### Discussion

The stack view ensures that the [`arrangedSubviews`](nsstackview/arrangedsubviews.md) array is always a subset of its [`subviews`](nsview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it is not already. If the view is already a subview, this operation does not alter the subview ordering.

## Parameters

- `view`: The view to add to the end of the   array.

## See Also

- [func insertArrangedSubview(NSView, at: Int)](nsstackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(NSView)](nsstackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.
- [var arrangedSubviews: [NSView]](nsstackview/arrangedsubviews.md)
  The array of views arranged by the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/addarrangedsubview(_:))*