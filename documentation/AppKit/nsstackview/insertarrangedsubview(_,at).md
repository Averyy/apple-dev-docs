# insertArrangedSubview(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the provided view to the array of arranged subviews at the specified index.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func insertArrangedSubview(_ view: NSView, at index: Int)
```

```objc
- (void) insertArrangedSubview:(NSView *) view atIndex:(NSInteger) index;
```

#### Discussion

If index is already occupied, the stack view increases the size of the [`arrangedSubviews`](./arrangedsubviews.md) array and shifts all of its contents at the index and above to the next higher space in the array. Then the stack view stores the provided view at the index.

The stack view also ensures that the [`arrangedSubviews`](./arrangedsubviews.md) array is always a subset of its [`subviews`](../nsview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it is not already. When adding subviews, the stack view appends the view to the end of its [`subviews`](../nsview/subviews.md) array. The index only affects the order of views in the [`arrangedSubviews`](./arrangedsubviews.md) array. It does not affect the ordering of views in the [`subviews`](../nsview/subviews.md) array.

## Parameters

- `view`: The view to be added to the array of arranged views managed by the stack.
- `index`: The index where the stack inserts the new view in its [`arrangedSubviews`](./arrangedsubviews.md) array. This value must not be greater than the number of views currently in this array. If the index is out of bounds, this method throws an [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) exception.

## See Also

### Managing the Arranged Subviews
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds the specified view to the end of the arranged subviews list.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.
- [var arrangedSubviews: [NSView]](./arrangedsubviews.md)
  The array of views arranged by the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/insertarrangedsubview(_:at:))*