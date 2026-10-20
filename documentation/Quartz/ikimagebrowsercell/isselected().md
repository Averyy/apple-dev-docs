# isSelected()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether the cell is selected.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func isSelected() -> Bool
```

```objc
- (BOOL) isSelected;
```

#### Return Value

[`true`](../../Swift/true.md) if the cell is selected, otherwise [`false`](../../Swift/false.md).

#### Discussion

Subclasses should not override this method.

## See Also

### Selection Handling
- [func selectionFrame() -> NSRect](./selectionframe%28%29.md)
  Returns the receiver’s selection frame rectangle, which defines the position of the selection rectangle in its [`IKImageBrowserView`](../ikimagebrowserview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/isselected())*