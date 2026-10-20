# setValidateSize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies whether the receiver’s size information is validated.

**Availability**:
- macOS

## Declaration

```swift
func setValidateSize(_ flag: Bool)
```

```objc
- (void) setValidateSize:(BOOL) flag;
```

## Parameters

- `flag`: [`true`](../../Swift/true.md) to assume that the size information in the receiver is correct. If `flag` is [`false`](../../Swift/false.md), the [`NSControl`](../nscontrol.md) method [`calcSize()`](../nscontrol/calcsize%28%29.md) will be invoked before any further drawing is done.

## See Also

### Resizing the Matrix and Its Cells
- [var autosizesCells: Bool](./autosizescells.md)
  A Boolean that indicates whether the cell sizes change when the receiver is resized.
- [func sizeToCells()](./sizetocells%28%29.md)
  Changes the width and the height of the receiver’s frame so it exactly contains the cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/setvalidatesize(_:))*