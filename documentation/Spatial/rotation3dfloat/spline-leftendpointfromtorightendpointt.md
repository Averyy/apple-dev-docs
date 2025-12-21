# spline(leftEndpoint:from:to:rightEndpoint:t:)

**Framework**: Spatial  
**Kind**: method

Returns an interpolated value between two rotations along a spherical cubic spline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func spline(leftEndpoint r0: Rotation3DFloat, from r1: Rotation3DFloat, to r2: Rotation3DFloat, rightEndpoint r3: Rotation3DFloat, t: Float) -> Rotation3DFloat
```

#### Return Value

A new rotation that’s the interpolated value between the two rotations along a spherical cubic spline.

#### Discussion

Use this function to smoothly interpolate between a sequence of rotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/spline(leftendpoint:from:to:rightendpoint:t:))*