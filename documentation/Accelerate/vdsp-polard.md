# vDSP_polarD

**Framework**: Accelerate  
**Kind**: func

Converts double-precision rectangular coordinates to polar coordinates, using the specified stride.

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
extern void vDSP_polarD(const double * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The function uses the following calculation to convert rectangular coordinates to polar coordinates:

```swift
for (n = 0; n < N; ++n)
{
    x = A[n*IA+0];
    y = A[n*IA+1];
    C[n*IC+0] = sqrt(x**2 + y**2);
    C[n*IC+1] = atan2(y, x);
}
```

Vector `A` defines the input Cartesian (x, y) pairs. The function writes polar (rho, theta) pairs, where rho is the radius and theta is the angle in the range `[-pi, pi]` to output vector `C`. `N` specifies the number of coordinate pairs in `A` and `C`.

Coordinate pairs are adjacent elements in the array, regardless of stride; stride is the distance from one coordinate pair to the next.

The following code shows how to convert a single pair of rectangular coordinates to their polar equivalent.

```swift
let x = 5.0
let y = 5.0

let rectangularCoordinates = [x, y]

var polarCoordinates: [Double] = [0, 0]

let stride = vDSP_Stride(2)
let n = vDSP_Length(1)

vDSP_polarD(rectangularCoordinates, stride,
            &polarCoordinates, stride,
            n)

let radius = polarCoordinates[0]
let angle = Measurement(value: polarCoordinates[1],
                        unit: UnitAngle.radians)
    .converted(to: UnitAngle.degrees)
    .value
```

On return, `radius` is `7.07`, and `angle` is `45`.

This function performs the inverse operation of [`vDSP_rectD`](vdsp_rectd.md), which converts polar to rectangular coordinates.

## Parameters

- `__A`: The input vector that contains adjacent pairs of coordinates.
- `__IA`: The distance between the adjacent coordinate pairs of elements in the input vector. This value must be an even number.
- `__C`: On output, the output vector that contains adjacent pairs of coordinates.
- `__IC`: The distance between the adjacent coordinate pairs of elements in the output vector. This value must be an even number.
- `__N`: The number of ordered pairs that the function processes.

## See Also

- [vDSP_polar](vdsp_polar.md)
  Converts single-precision rectangular coordinates to polar coordinates, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_polard)*