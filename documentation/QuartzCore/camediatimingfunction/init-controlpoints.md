# init(controlPoints:_:_:_:)

**Framework**: Core Animation  
**Kind**: init

Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)
```

#### Return Value

An instance of `CAMediaTimingFunction` with the timing function specified by the provided control points.

#### Discussion

The end points of the Bézier curve are automatically set to (0.0,0.0) and (1.0,1.0). The control points defining the Bézier curve are: [(0.0,0.0), (`c1x`,`c1y`), (`c2x`,`c2y`), (1.0,1.0)].

## Parameters

- `c1x`: A floating point number representing the x position of the c1 control point.
- `c1y`: A floating point number representing the y position of the c1 control point.
- `c2x`: A floating point number representing the x position of the c2 control point.
- `c2y`: A floating point number representing the y position of the c2 control point.

## See Also

- [convenience init(name: CAMediaTimingFunctionName)](camediatimingfunction/init(name:).md)
  Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/init(controlpoints:_:_:_:))*