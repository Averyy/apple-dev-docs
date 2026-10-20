# intersect(with:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func intersect(with s2: CIFilterShape) -> CIFilterShape
```

```objc
- (CIFilterShape *) intersectWith:(CIFilterShape *) s2;
```

#### Return Value

The filter shape object that results from the intersection.

## Parameters

- `s2`: A filter shape object.

## See Also

### Modifying a Filter Shape
- [func insetBy(x: Int32, y: Int32) -> CIFilterShape](./insetby%28x,y%29.md)
  Modifies a filter shape object so that it is inset by the specified x and y values.
- [func intersect(with: CGRect) -> CIFilterShape](./intersect%28with%29-2o2n8.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func transform(by: CGAffineTransform, interior: Bool) -> CIFilterShape](./transform%28by,interior%29.md)
  Creates a filter shape that results from applying a transform to the current filter shape.
- [func union(with: CIFilterShape) -> CIFilterShape](./union%28with%29-52mnd.md)
  Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [func union(with: CGRect) -> CIFilterShape](./union%28with%29-75ebo.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape/intersect(with:)-8iw)*