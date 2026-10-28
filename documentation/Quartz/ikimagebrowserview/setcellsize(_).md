# setCellSize(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the cell  size.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setCellSize(_ size: NSSize)
```

```objc
- (void) setCellSize:(NSSize) size;
```

## Discussion

You must use `setCellSize` or [`setZoomValue(_:)`](./setzoomvalue%28_%29.md), but not both. Setting the zoom value changes the cell size, and vice versa.

## Parameters

- `size`: The size to set.

## See Also

### Related Documentation
- [func setZoomValue(Float)](./setzoomvalue%28_%29.md)
  Sets the zoom value.
### Setting and Getting Cell Size
- [func cellSize() -> NSSize](./cellsize%28%29.md)
  Returns the cell size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcellsize(_:))*