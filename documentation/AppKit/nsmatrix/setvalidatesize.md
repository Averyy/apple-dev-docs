# setValidateSize(_:)

**Framework**: AppKit  
**Kind**: method

Specifies whether the receiver’s size information is validated.

**Availability**:
- macOS ?+

## Declaration

```swift
func setValidateSize(_ flag: Bool)
```

## Parameters

- `flag`: [`true`](https://developer.apple.com/documentation/swift/true) to assume that the size information in the receiver is correct. If `flag` is [`false`](https://developer.apple.com/documentation/swift/false), the [`NSControl`](nscontrol.md) method [`calcSize()`](nscontrol/calcsize().md) will be invoked before any further drawing is done.

## See Also

- [var autosizesCells: Bool](nsmatrix/autosizescells.md)
  A Boolean that indicates whether the cell sizes change when the receiver is resized.
- [func sizeToCells()](nsmatrix/sizetocells.md)
  Changes the width and the height of the receiver’s frame so it exactly contains the cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/setvalidatesize(_:))*