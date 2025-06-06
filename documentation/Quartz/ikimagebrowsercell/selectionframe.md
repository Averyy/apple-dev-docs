# selectionFrame()

**Framework**: Quartz  
**Kind**: method

Returns the receiver’s selection frame rectangle, which defines the position of the selection rectangle in its [`IKImageBrowserView`](ikimagebrowserview.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func selectionFrame() -> NSRect
```

#### Return Value

The cells selection frame, in the `IKImageBrowserView` coordinate space.

#### Discussion

Subclasses can override this method to customize the position of the selection frame.

## See Also

- [func isSelected() -> Bool](ikimagebrowsercell/isselected.md)
  Returns whether the cell is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/selectionframe())*