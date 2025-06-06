# CapturedRoom.Surface

**Framework**: RoomPlan  
**Kind**: struct

A 2D area in a room that the framework identifies as a surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Surface
```

#### Overview

A captured room ([`CapturedRoom`](capturedroom.md)) contains an arrays of surfaces that it identifies in a scan, such as its [`doors`](capturedroom/doors.md), [`openings`](capturedroom/openings.md), [`walls`](capturedroom/walls.md), and [`windows`](capturedroom/windows.md).

## Topics

### Creating a surface
- [init(from: any Decoder) throws](capturedroom/surface/init(from:).md)
  Creates a surface by deserializing the specified decoder.
### Identifying a surface
- [var identifier: UUID](capturedroom/surface/identifier.md)
  A unique alphanumeric value that the framework assigns the surface.
- [var parentIdentifier: UUID?](capturedroom/surface/parentidentifier.md)
  A unique alphanumeric value that identifies a surface’s parent surface.
- [var category: CapturedRoom.Surface.Category](capturedroom/surface/category-swift.property.md)
  A classification that the captured room assigns the surface.
- [CapturedRoom.Surface.Category](capturedroom/surface/category-swift.enum.md)
  Classifications of a surface in a captured room.
- [var confidence: CapturedRoom.Confidence](capturedroom/surface/confidence.md)
  A level of certainty in the surface’s category.
### Positioning and sizing a surface
- [var transform: simd_float4x4](capturedroom/surface/transform.md)
  A matrix that defines the surface’s position and orientation in the scene.
- [var dimensions: simd_float3](capturedroom/surface/dimensions.md)
  A bounding box that contains the surface.
- [var story: Int](capturedroom/surface/story.md)
  indicator for which story, level, or floor
### Shaping a surface
- [var completedEdges: Set<CapturedRoom.Surface.Edge>](capturedroom/surface/completededges.md)
  An array of edges that outline the surface.
- [CapturedRoom.Surface.Edge](capturedroom/surface/edge.md)
  An object that represents a single edge of a surface.
- [var curve: CapturedRoom.Surface.Curve?](capturedroom/surface/curve-swift.property.md)
  An object that represents the curve of a surface.
- [CapturedRoom.Surface.Curve](capturedroom/surface/curve-swift.struct.md)
  An object that represents a single curve of a surface.
- [var polygonCorners: [simd_float3]](capturedroom/surface/polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.
### Serializing a surface
- [func encode(to: any Encoder) throws](capturedroom/surface/encode(to:).md)
  Serializes a surface to the specified encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var identifier: UUID](capturedroom/identifier.md)
  A unique alphanumeric value that the framework assigns the room.
- [var story: Int](capturedroom/story.md)
  The story, floor number, or level on which the captured room resides within a larger structure.
- [var floors: [CapturedRoom.Surface]](capturedroom/floors.md)
  An array of floors that the framework identifies during a scan.
- [var doors: [CapturedRoom.Surface]](capturedroom/doors.md)
  An array of doors that the framework identifies during a scan.
- [var objects: [CapturedRoom.Object]](capturedroom/objects.md)
  An array of objects that the framework identifies during a scan.
- [CapturedRoom.Object](capturedroom/object.md)
  A 3D area in a room that the framework identifies as an object.
- [var openings: [CapturedRoom.Surface]](capturedroom/openings.md)
  An array of openings that the framework identifies during a scan.
- [var walls: [CapturedRoom.Surface]](capturedroom/walls.md)
  An array of walls that the framework identifies during a scan.
- [var windows: [CapturedRoom.Surface]](capturedroom/windows.md)
  An array of windows that the framework identifies during a scan.
- [var sections: [CapturedRoom.Section]](capturedroom/sections.md)
  One or more room types that the framework observes in the room.
- [CapturedRoom.Section](capturedroom/section.md)
  An object that identifies a particular area in a captured room in relation to common types of room areas in a building.
- [CapturedRoom.Confidence](capturedroom/confidence.md)
  Levels of certainty in the classification of a particular detail in a scan.
- [var version: Int](capturedroom/version.md)
  A version number for the captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface)*