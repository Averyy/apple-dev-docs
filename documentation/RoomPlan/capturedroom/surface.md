# CapturedRoom.Surface

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

A 2D area in a room that the framework identifies as a surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Surface
```

## Overview

A captured room ([`CapturedRoom`](../capturedroom.md)) contains an arrays of surfaces that it identifies in a scan, such as its [`doors`](./doors.md), [`openings`](./openings.md), [`walls`](./walls.md), and [`windows`](./windows.md).

## Topics

### Creating a surface
- [init(from: any Decoder) throws](./surface/init%28from%29.md)
  Creates a surface by deserializing the specified decoder.
### Identifying a surface
- [var identifier: UUID](./surface/identifier.md)
  A unique alphanumeric value that the framework assigns the surface.
- [var parentIdentifier: UUID?](./surface/parentidentifier.md)
  A unique alphanumeric value that identifies a surface’s parent surface.
- [var category: CapturedRoom.Surface.Category](./surface/category-swift.property.md)
  A classification that the captured room assigns the surface.
- [CapturedRoom.Surface.Category](./surface/category-swift.enum.md)
  Classifications of a surface in a captured room.
- [var confidence: CapturedRoom.Confidence](./surface/confidence.md)
  A level of certainty in the surface’s category.
### Positioning and sizing a surface
- [var transform: simd_float4x4](./surface/transform.md)
  A matrix that defines the surface’s position and orientation in the scene.
- [var dimensions: simd_float3](./surface/dimensions.md)
  A bounding box that contains the surface.
- [var story: Int](./surface/story.md)
  indicator for which story, level, or floor
### Shaping a surface
- [var completedEdges: Set<CapturedRoom.Surface.Edge>](./surface/completededges.md)
  An array of edges that outline the surface.
- [CapturedRoom.Surface.Edge](./surface/edge.md)
  An object that represents a single edge of a surface.
- [var curve: CapturedRoom.Surface.Curve?](./surface/curve-swift.property.md)
  An object that represents the curve of a surface.
- [CapturedRoom.Surface.Curve](./surface/curve-swift.struct.md)
  An object that represents a single curve of a surface.
- [var polygonCorners: [simd_float3]](./surface/polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.
### Serializing a surface
- [func encode(to: any Encoder) throws](./surface/encode%28to%29.md)
  Serializes a surface to the specified encoder.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting room details
- [var identifier: UUID](./identifier.md)
  A unique alphanumeric value that the framework assigns the room.
- [var story: Int](./story.md)
  The story, floor number, or level on which the captured room resides within a larger structure.
- [var floors: [CapturedRoom.Surface]](./floors.md)
  An array of floors that the framework identifies during a scan.
- [var doors: [CapturedRoom.Surface]](./doors.md)
  An array of doors that the framework identifies during a scan.
- [var objects: [CapturedRoom.Object]](./objects.md)
  An array of objects that the framework identifies during a scan.
- [CapturedRoom.Object](./object.md)
  A 3D area in a room that the framework identifies as an object.
- [var openings: [CapturedRoom.Surface]](./openings.md)
  An array of openings that the framework identifies during a scan.
- [var walls: [CapturedRoom.Surface]](./walls.md)
  An array of walls that the framework identifies during a scan.
- [var windows: [CapturedRoom.Surface]](./windows.md)
  An array of windows that the framework identifies during a scan.
- [var sections: [CapturedRoom.Section]](./sections.md)
  One or more room types that the framework observes in the room.
- [CapturedRoom.Section](./section.md)
  An object that identifies a particular area in a captured room in relation to common types of room areas in a building.
- [CapturedRoom.Confidence](./confidence.md)
  Levels of certainty in the classification of a particular detail in a scan.
- [var version: Int](./version.md)
  A version number for the captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface)*