# generatePlane(width:height:cornerRadius:)

**Framework**: Realitykit  
**Kind**: method

Creates a new rectangle mesh with the specified dimensions in the entity’s xy-plane.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generatePlane(width: Float, height: Float, cornerRadius: Float = 0) -> MeshResource
```

#### Return Value

The rectangle mesh.

#### Discussion

The rectangle is centered at the entity’s origin and aligned with its x and y axes. The surface normal points along the z-axis. The depth along the z-axis is 0.

> **Note**: The xy-plane is a plane that aligns with the x and y axes.

## Parameters

- `width`: The width, in meters, of the rectangle along the x-axis.
- `height`: The height, in meters, of the rectangle along the y-axis.
- `cornerRadius`: A corner radius in the form of a circular arc, with   curvature that transitions abruptly from   to   at the boundary   between the edge and the corner.

## See Also

- [static func generatePlane(width: Float, depth: Float, cornerRadius: Float) -> MeshResource](meshresource/generateplane(width:depth:cornerradius:).md)
  Creates a new rectangle mesh with the specified dimensions in the entity’s xz-plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generateplane(width:height:cornerradius:))*