# invalidateIntrinsicContentSize(for:)

**Framework**: AppKit  
**Kind**: method

Notifies the control that the intrinsic content size for its cell is no longer valid.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func invalidateIntrinsicContentSize(for cell: NSCell)
```

#### Discussion

Controls determine their intrinsic content size based on the cell size for a given bounds returned by their cell. When the content of the cell changes in a way that would change the return value of [`cellSize(forBounds:)`](nscell/cellsize(forbounds:).md), the cell needs to call this method to notify its control that its intrinsic size is no longer valid.

## Parameters

- `cell`: The cell whose intrinsic content size has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/invalidateintrinsiccontentsize(for:))*