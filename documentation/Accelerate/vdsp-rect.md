# vDSP_rect

**Framework**: Accelerate  
**Kind**: func

Converts single-precision polar coordinates to rectangular coordinates, using the specified stride.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_rect(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The function uses the following calculation to convert polar coordinates to rectangular coordinates:

```swift
for (n = 0; n < N; ++n)
{
    r     = A[n*IA+0];
    theta = A[n*IA+1];
    C[n*IC+0] = r * cos(theta);
    C[n*IC+1] = r * sin(theta);
}
```

Vector `A` defines the input polar (rho, theta) pairs, where rho is the radius and theta is the angle in the range `[-pi, pi]`. The function writes Cartesian (x, y) pairs to the output vector `C`. `N` specifies the number of coordinate pairs in `A` and `C`.

Coordinate pairs are adjacent elements in the array, regardless of stride; stride is the distance from one coordinate pair to the next.

The following code shows how to convert an angle-radius pair (with the angle specified in degress) to its rectangular equivalent.

```swift
    let angle = Measurement(value: 45,
                            unit: UnitAngle.degrees)
        .converted(to: UnitAngle.radians)
        .value

    let radius = sqrt(25.0 + 25.0)

    let polarCoordinates = [radius, angle].map { Float($0) }

    var rectangularCoordinates: [Float] = [0, 0]

    let stride = vDSP_Stride(2)
    let n = vDSP_Length(1)

    vDSP_rect(polarCoordinates, stride,
               &rectangularCoordinates, stride,
               n)
```

On return, `rectangularCoordinates` contains `[5, 5]`.

This function performs the inverse operation of [`vDSP_polar`](vdsp_polar.md), which converts rectangular to polar coordinates.

## Parameters

- `__A`: The input vector that contains adjacent pairs of coordinates.
- `__IA`: The distance between the adjacent coordinate pairs of elements in the input vector. This value must be an even number.
- `__C`: On output, the output vector that contains adjacent pairs of coordinates.
- `__IC`: The distance between the adjacent coordinate pairs of elements in the output vector. This value must be an even number.
- `__N`: The number of ordered pairs that the function processes.

## See Also

- [vDSP_rectD](vdsp_rectd.md)
  Converts double-precision polar coordinates to rectangular coordinates, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_rect)*