# convert(rectangularCoordinates:toPolarCoordinates:)

**Framework**: Accelerate  
**Kind**: method

Converts single-precision rectangular coordinates to polar coordinates.

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
static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates polarCoordinates: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

#### Discussion

The function calls the underlying [`vDSP_polarD`](vdsp_polard.md) function to convert the input angle-radius pairs to Cartesian x-y pairs.

The following code shows how to convert a set of Cartesian coordinates to its angle-radius pair (with the angle specified in degress) equivalent:

```swift
    let rectangularCoordinates = [ 5.0, 5.0 ]

    let polarCoordinates = [Double](unsafeUninitializedCapacity: 2) {
        buffer,initializedCount in
        
        vDSP.convert(
            rectangularCoordinates: rectangularCoordinates,
            toPolarCoordinates: &buffer
        )
        
        initializedCount = 2
    }
    
    let radius = polarCoordinates[0]
    let angle = Measurement(value: polarCoordinates[1],
                            unit: UnitAngle.radians)
        .converted(to: UnitAngle.degrees)
        .value
    
    // Prints "7.07 45.0".
    print(radius, angle)
```

## Parameters

- `rectangularCoordinates`: The source rectangular coordinates.
- `polarCoordinates`: On output, the polar coordinates.

## See Also

- [static func rectangularToPolar<U>(U) -> [Float]](vdsp/rectangulartopolar(_:)-5p4kg.md)
  Returns single-precision polar coordinates converted from rectangular coordinates.
- [static func rectangularToPolar<U>(U) -> [Double]](vdsp/rectangulartopolar(_:)-3txg1.md)
  Returns double-precision polar coordinates converted from rectangular coordinates.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](vdsp/convert(rectangularcoordinates:topolarcoordinates:)-84131.md)
  Converts double-precision rectangular coordinates to polar coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(rectangularcoordinates:topolarcoordinates:)-1zi4t)*