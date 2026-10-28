# addArrangedSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified view to the end of the arranged subviews list.

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

The stack view ensures that the [`arrangedSubviews`](./arrangedsubviews.md) array is always a subset of its [`subviews`](../nsview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it is not already. If the view is already a subview, this operation does not alter the subview ordering.

## Parameters

- `view`: The view to add to the end of the [`arrangedSubviews`](./arrangedsubviews.md) array.

## See Also

### Managing the Arranged Subviews
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views arranged by the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/addarrangedsubview(_:))*