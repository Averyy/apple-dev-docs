# generateCylinder(height:radius:)

**Framework**: RealityKit  
**Kind**: method

Creates a new cylinder mesh with the specified dimensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generateCylinder(height: Float, radius: Float) -> MeshResource
```

#### Discussion

The cylinder is centered at the local origin.

## Parameters

- `height`: The height of the cylinder in meters [m].
- `radius`: The radius of the cylinder in meters [m].

## See Also

- [static func generateSphere(radius: Float) -> MeshResource](meshresource/generatesphere(radius:).md)
  Creates a new sphere mesh with the specified radius.
- [static generateCone(height:radius:)](meshresource/generatecone(height:radius:).md)
  Creates a new cone mesh with the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatecylinder(height:radius:))*