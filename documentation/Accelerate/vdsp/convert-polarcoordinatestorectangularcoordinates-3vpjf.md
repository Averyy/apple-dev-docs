# convert(polarCoordinates:toRectangularCoordinates:)

**Framework**: Accelerate  
**Kind**: method

Converts single-precision polar coordinates to rectangular coordinates.

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
static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates rectangularCoordinates: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
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

    let rectangularCoordinates = [Float](unsafeUninitializedCapacity: 2) {
        buffer,initializedCount in
        
        vDSP.convert(
            polarCoordinates: polarCoordinates,
            toRectangularCoordinates: &buffer
        )
        
        initializedCount = 2
    }
    
    // Prints "[5.0, 5.0]".
    print(rectangularCoordinates)
```

## Parameters

- `polarCoordinates`: The source polar coordinates.
- `rectangularCoordinates`: On output, the rectangular coordinates.

## See Also

- [static func polarToRectangular<U>(U) -> [Float]](vdsp/polartorectangular(_:)-8upqj.md)
  Returns single-precision rectangular coordinates converted from polar coordinates.
- [static func polarToRectangular<U>(U) -> [Double]](vdsp/polartorectangular(_:)-jgv8.md)
  Returns double-precision rectangular coordinates converted from polar coordinates.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](vdsp/convert(polarcoordinates:torectangularcoordinates:)-22zz0.md)
  Converts double-precision polar coordinates to rectangular coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(polarcoordinates:torectangularcoordinates:)-3vpjf)*