# generateSphere(radius:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a new sphere mesh with the specified radius.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency static func generateSphere(radius: Float) -> MeshResource
```

#### Return Value

A sphere mesh.

#### Discussion

The sphere is centered at the entity’s origin.

## Parameters

- `radius`: The radius, in meters, of the sphere.

## See Also

### Creating a primitive shape
- [static func generateCone(height: Float, radius: Float) -> MeshResource](./generatecone%28height,radius%29.md)
  Creates a new cone mesh with the specified dimensions.
- [static func generateCylinder(height: Float, radius: Float) -> MeshResource](./generatecylinder%28height,radius%29.md)
  Creates a new cylinder mesh with the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatesphere(radius:))*