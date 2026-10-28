# intersects(sphereOrigin:sphereRadius:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func intersects(sphereOrigin: Point3DFloat, sphereRadius: Float) -> Bool
```

```c
static bool SPRay3DFloatIntersectsSphere(SPRay3DFloat ray, SPPoint3DFloat sphereOrigin, float sphereRadius);
```

## Return Value

A  Boolean value that indicates whether the ray intersects the sphere.

## Discussion

Returns a Boolean value that indicates whether the ray intersects a specified sphere.

## Parameters

- `sphereOrigin`: A point structure that defines the center of the sphere.
- `sphereRadius`: The radius of the sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/intersects(sphereorigin:sphereradius:))*