# init(named:offsetPosition:offsetOrientation:)

**Framework**: RealityKit  
**Kind**: init

Creates a geometric pin that identifies a local position and orientation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(named name: String, offsetPosition: SIMD3<Float> = SIMD3<Float>(0, 0, 0), offsetOrientation: simd_quatf = simd_quatf(ix: 0, iy: 0, iz: 0, r: 1))
```

## Parameters

- `name`: Name of the   in the namespace of the owning entity.
- `offsetPosition`: Adjustment of the   position in the local coordinate frame.
- `offsetOrientation`: Adjustment of the   orientation in the local coordinate frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/geometricpin/init(named:offsetposition:offsetorientation:))*