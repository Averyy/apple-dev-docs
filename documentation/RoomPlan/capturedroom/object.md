# CapturedRoom.Object

**Framework**: RoomPlan  
**Kind**: struct

A 3D area in a room that the framework identifies as an object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Object
```

#### Overview

A captured room contains an array of this type for the objects ([`objects`](capturedroom/objects.md)) it identifies.

## Topics

### Creating an object
- [init(from: any Decoder) throws](capturedroom/object/init(from:).md)
  Creates an object by deserializing the specified decoder.
### Identifying an object
- [var identifier: UUID](capturedroom/object/identifier.md)
  A unique alphanumeric value that the framework assigns the object.
- [var parentIdentifier: UUID?](capturedroom/object/parentidentifier.md)
  A unique alphanumeric value that identifies the object’s parent object or surface.
- [var category: CapturedRoom.Object.Category](capturedroom/object/category-swift.property.md)
  A classification that the captured room assigns the object.
- [CapturedRoom.Object.Category](capturedroom/object/category-swift.enum.md)
  Classifications of an object in a captured room.
- [var confidence: CapturedRoom.Confidence](capturedroom/object/confidence.md)
  A level of certainty in the object’s category.
### Positioning and sizing an object
- [var transform: simd_float4x4](capturedroom/object/transform.md)
  A matrix that defines the object’s position and orientation in the room.
- [var dimensions: simd_float3](capturedroom/object/dimensions.md)
  A bounding box sized to the object’s extremities.
- [var story: Int](capturedroom/object/story.md)
  The floor number or level on which the object resides.
### Describing an object
- [var attributes: [any CapturedRoomAttribute]](capturedroom/object/attributes.md)
  A collection of details that describe a particular object in the room.
- [func attribute<T>(of: T.Type) -> T?](capturedroom/object/attribute(of:).md)
  Checks an object for specific attribute types.
### Serializing an object
- [func encode(to: any Encoder) throws](capturedroom/object/encode(to:).md)
  Serializes an object to the specified encoder.

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
- [CapturedRoom.Surface](capturedroom/surface.md)
  A 2D area in a room that the framework identifies as a surface.
- [var doors: [CapturedRoom.Surface]](capturedroom/doors.md)
  An array of doors that the framework identifies during a scan.
- [var objects: [CapturedRoom.Object]](capturedroom/objects.md)
  An array of objects that the framework identifies during a scan.
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

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object)*