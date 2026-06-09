# init(position:normal:radius:)

**Framework**: RealityKit  
**Kind**: init

Creates a curved portal plane (cylinder) with position, normal, and curvature.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.0+
- macOS 27.0+ (Beta)
- tvOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(position: SIMD3<Float>, normal: SIMD3<Float>, radius: Float)
```

#### Discussion

The curved plane represents an infinite cylindrical surface in portal-local space, equivalent to the radius behavior in `UICurvatureComponent`. The plane’s position and normal define the cylinder’s center axis orientation, while radius defines how much the plane bends.

## Parameters

- `position`: The center position of the plane in portal-local space
- `normal`: The axis direction along which the cylinder extends (for curved planes)
- `radius`: The cylinder’s radius. Zero for flat planes, positive for curved. Defaults to 0 (flat plane).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/plane/init(position:normal:radius:))*