# setCellSize(_:)

**Framework**: Quartz  
**Kind**: method

Sets the cell  size.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setCellSize(_ size: NSSize)
```

#### Discussion

You must use `setCellSize` or [`setZoomValue(_:)`](ikimagebrowserview/setzoomvalue(_:).md), but not both. Setting the zoom value changes the cell size, and vice versa.

## Parameters

- `size`: The size to set.

## See Also

- [func setZoomValue(Float)](ikimagebrowserview/setzoomvalue(_:).md)
  Sets the zoom value.
- [func cellSize() -> NSSize](ikimagebrowserview/cellsize.md)
  Returns the cell size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcellsize(_:))*