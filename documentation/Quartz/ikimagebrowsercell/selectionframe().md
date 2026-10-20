# selectionFrame()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s selection frame rectangle, which defines the position of the selection rectangle in its [`IKImageBrowserView`](../ikimagebrowserview.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func selectionFrame() -> NSRect
```

```objc
- (NSRect) selectionFrame;
```

#### Return Value

The cells selection frame, in the `IKImageBrowserView` coordinate space.

#### Discussion

Subclasses can override this method to customize the position of the selection frame.

## See Also

### Selection Handling
- [func isSelected() -> Bool](./isselected%28%29.md)
  Returns whether the cell is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/selectionframe())*