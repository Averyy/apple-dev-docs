# generatePlane(width:depth:cornerRadius:)

**Framework**: RealityKit  
**Kind**: method

Creates a new rectangle mesh with the specified dimensions in the entity’s xz-plane.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generatePlane(width: Float, depth: Float, cornerRadius: Float = 0) -> MeshResource
```

#### Return Value

The rectangle mesh.

#### Discussion

The rectangle is centered at the entity’s origin and aligned with its x and y axes. The surface normal points along the y-axis. The depth along the y-axis is 0.

> **Note**: The xz-plane is a plane that aligns with the x and z axes.

## Parameters

- `width`: The width, in meters, of the rectangle along the x-axis.
- `depth`: The depth, in meters, of the rectangle along the z-axis.
- `cornerRadius`: A corner radius in the form of a circular arc, with   curvature that transitions abruptly from   to   at the boundary   between the edge and the corner.

## See Also

- [static func generatePlane(width: Float, height: Float, cornerRadius: Float) -> MeshResource](meshresource/generateplane(width:height:cornerradius:).md)
  Creates a new rectangle mesh with the specified dimensions in the entity’s xy-plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generateplane(width:depth:cornerradius:))*