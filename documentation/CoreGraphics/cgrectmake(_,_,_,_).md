# CGRectMake(_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a rectangle with the specified coordinate and size values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CGRectMake(_ x: CGFloat, _ y: CGFloat, _ width: CGFloat, _ height: CGFloat) -> CGRect
```

```c
static CGRect CGRectMake(CGFloat x, CGFloat y, CGFloat width, CGFloat height);
```

#### Return Value

A rectangle with the specified location and dimensions.

## Parameters

- `x`: The x-coordinate of the rectangle’s origin point.
- `y`: The y-coordinate of the rectangle’s origin point.
- `width`: The width of the rectangle.
- `height`: The height of the rectangle.

## See Also

### Creating a Geometric Primitive from Values
- [func CGPointMake(CGFloat, CGFloat) -> CGPoint](./cgpointmake%28_,_%29.md)
  Returns a point with the specified coordinates.
- [func CGSizeMake(CGFloat, CGFloat) -> CGSize](./cgsizemake%28_,_%29.md)
  Returns a size with the specified dimension values.
- [func CGVectorMake(CGFloat, CGFloat) -> CGVector](./cgvectormake%28_,_%29.md)
  Returns a vector with the specified dimension values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectmake(_:_:_:_:))*