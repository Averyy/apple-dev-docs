# CapturedRoom.Object

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

A 3D area in a room that the framework identifies as an object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Object
```

## Overview

A captured room contains an array of this type for the objects ([`objects`](./objects.md)) it identifies.

## Topics

### Creating an object
- [init(from: any Decoder) throws](./object/init%28from%29.md)
  Creates an object by deserializing the specified decoder.
### Identifying an object
- [var identifier: UUID](./object/identifier.md)
  A unique alphanumeric value that the framework assigns the object.
- [var parentIdentifier: UUID?](./object/parentidentifier.md)
  A unique alphanumeric value that identifies the object’s parent object or surface.
- [var category: CapturedRoom.Object.Category](./object/category-swift.property.md)
  A classification that the captured room assigns the object.
- [CapturedRoom.Object.Category](./object/category-swift.enum.md)
  Classifications of an object in a captured room.
- [var confidence: CapturedRoom.Confidence](./object/confidence.md)
  A level of certainty in the object’s category.
### Positioning and sizing an object
- [var transform: simd_float4x4](./object/transform.md)
  A matrix that defines the object’s position and orientation in the room.
- [var dimensions: simd_float3](./object/dimensions.md)
  A bounding box sized to the object’s extremities.
- [var story: Int](./object/story.md)
  The floor number or level on which the object resides.
### Describing an object
- [var attributes: [any CapturedRoomAttribute]](./object/attributes.md)
  A collection of details that describe a particular object in the room.
- [func attribute<T>(of: T.Type) -> T?](./object/attribute%28of%29.md)
  Checks an object for specific attribute types.
### Serializing an object
- [func encode(to: any Encoder) throws](./object/encode%28to%29.md)
  Serializes an object to the specified encoder.

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
- [CapturedRoom.Surface](./surface.md)
  A 2D area in a room that the framework identifies as a surface.
- [var doors: [CapturedRoom.Surface]](./doors.md)
  An array of doors that the framework identifies during a scan.
- [var objects: [CapturedRoom.Object]](./objects.md)
  An array of objects that the framework identifies during a scan.
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

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object)*