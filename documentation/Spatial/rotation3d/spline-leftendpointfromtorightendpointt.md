# spline(leftEndpoint:from:to:rightEndpoint:t:)

**Framework**: Spatial  
**Kind**: method

Returns an interpolated value between two rotations along a spherical cubic spline.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
static func spline(leftEndpoint r0: Rotation3D, from r1: Rotation3D, to r2: Rotation3D, rightEndpoint r3: Rotation3D, t: Double) -> Rotation3D
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/spline(leftendpoint:from:to:rightendpoint:t:))*