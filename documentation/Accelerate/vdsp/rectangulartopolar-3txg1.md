# rectangularToPolar(_:)

**Framework**: Accelerate  
**Kind**: method

Returns double-precision polar coordinates converted from rectangular coordinates.

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
static func rectangularToPolar<U>(_ rectangularCoordinates: U) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

The function calls the underlying [`vDSP_polar`](vdsp_polar.md) function to convert the input angle-radius pairs to Cartesian x-y pairs.

The following code shows how to convert a set of Cartesian coordinates to its angle-radius pair (with the angle specified in degress) equivalent:

```swift
    let rectangularCoordinates: [Float] = [ 5.0, 5.0 ]

    let polarCoordinates = vDSP.rectangularToPolar(rectangularCoordinates)
    
    let radius = polarCoordinates[0]
    let angle = Measurement(value: Double(polarCoordinates[1]),
                            unit: UnitAngle.radians)
        .converted(to: UnitAngle.degrees)
        .value
    
    // Prints "7.07 45.0".
    print(radius, angle)
```

## Parameters

- `rectangularCoordinates`: The source rectangular coordinates.

## See Also

- [static func rectangularToPolar<U>(U) -> [Float]](vdsp/rectangulartopolar(_:)-5p4kg.md)
  Returns single-precision polar coordinates converted from rectangular coordinates.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](vdsp/convert(rectangularcoordinates:topolarcoordinates:)-1zi4t.md)
  Converts single-precision rectangular coordinates to polar coordinates.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](vdsp/convert(rectangularcoordinates:topolarcoordinates:)-84131.md)
  Converts double-precision rectangular coordinates to polar coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/rectangulartopolar(_:)-3txg1)*