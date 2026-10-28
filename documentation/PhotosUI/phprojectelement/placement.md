# placement

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A rectangle defining where an element is placed in grid space coordinates.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var placement: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect placement;
```

## Discussion

For layout grids with more than one column, the values in the rectangle will always have integer value.  For fixed layouts, rectangle values will be in fractional unit values.

If suggested placement could not be determined at the time of project creation, the placement will contain [`CGRectNull`](../../CoreGraphics/cgrectnull.md).

For example, a rect of `(0,` `0,` `3,` `4)` represents a placement in the upper-left corner of the layout grid, with 3 grid units of width and 4 grid units of height.

## See Also

### Describing Project Elements
- [var weight: Double](./weight.md)
  A value between 0 and 1 representing relative significance of the element in its section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectelement/placement)*