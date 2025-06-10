# polarToRectangular(_:)

**Framework**: Accelerate  
**Kind**: method

Returns single-precision rectangular coordinates converted from polar coordinates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func polarToRectangular<U>(_ polarCoordinates: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

#### Discussion

The function calls the underlying [`vDSP_rect`](vdsp_rect.md) function to convert the input angle-radius pairs to Cartesian x-y pairs.

The following code shows how to convert an angle-radius pair (with the angle specified in degress) to its rectangular equivalent:

```swift
    let angle = Measurement(value: 45,
                            unit: UnitAngle.degrees)
        .converted(to: UnitAngle.radians)
        .value

    let radius = sqrt(25.0 + 25.0)

    let polarCoordinates = [radius, angle].map { Float($0) }

    let rectangularCoordinates = vDSP.polarToRectangular(polarCoordinates)
    
    // Prints "[5.0, 5.0]".
    print(rectangularCoordinates)
```

## Parameters

- `polarCoordinates`: The source polar coordinates.

## See Also

- [static func polarToRectangular<U>(U) -> [Double]](vdsp/polartorectangular(_:)-jgv8.md)
  Returns double-precision rectangular coordinates converted from polar coordinates.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](vdsp/convert(polarcoordinates:torectangularcoordinates:)-3vpjf.md)
  Converts single-precision polar coordinates to rectangular coordinates.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](vdsp/convert(polarcoordinates:torectangularcoordinates:)-22zz0.md)
  Converts double-precision polar coordinates to rectangular coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/polartorectangular(_:)-8upqj)*