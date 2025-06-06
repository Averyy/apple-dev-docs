# setValidateSize(_:)

**Framework**: AppKit  
**Kind**: method

Specifies whether the receiver’s size information is validated.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setValidateSize(_ flag: Bool)
```

## Parameters

- `flag`:   to assume that the size information in the receiver is correct. If   is  , the   method   will be invoked before any further drawing is done.

## See Also

- [var autosizesCells: Bool](nsmatrix/autosizescells.md)
  A Boolean that indicates whether the cell sizes change when the receiver is resized.
- [func sizeToCells()](nsmatrix/sizetocells.md)
  Changes the width and the height of the receiver’s frame so it exactly contains the cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/setvalidatesize(_:))*