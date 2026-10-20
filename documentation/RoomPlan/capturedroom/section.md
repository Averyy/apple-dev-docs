# CapturedRoom.Section

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

An object that identifies a particular area in a captured room in relation to common types of room areas in a building.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Section
```

#### Overview

When RoomPlan recognizes a captured room as one of the common kinds of room areas, such as a living room, the framework adds an instance of this structure to the room’s [`sections`](./sections.md) array.

The section instance provides:

- A label type for the common area ([`label`](./section/label-swift.property.md)), such as  [`CapturedRoom.Section.Label.livingRoom`](./section/label-swift.enum/livingroom.md)
- A center point ([`center`](./section/center.md)), that generally locates the area within the room
- A story ([`story`](./section/story.md)), that identifies a floor number for the area in the building

In a larger room, the framework may identify multiple types of areas, for example, a kitchen and a dining room. In that case, the `sections` array contains both, [`CapturedRoom.Section.Label.kitchen`](./section/label-swift.enum/kitchen.md) and [`CapturedRoom.Section.Label.diningRoom`](./section/label-swift.enum/diningroom.md), and their `center` points distinguish their individual locations within the room.

## Topics

### Creating a section
- [init(from: any Decoder) throws](./section/init%28from%29.md)
  Creates a section by deserializing the given decoder.
### Describing a section
- [var label: CapturedRoom.Section.Label](./section/label-swift.property.md)
  A textual name for the section.
- [CapturedRoom.Section.Label](./section/label-swift.enum.md)
  Textual names for one part of a larger structure.
### Locating a section
- [var story: Int](./section/story.md)
  The story, floor number, or level on which the section resides in a structure.
- [var center: simd_float3](./section/center.md)
  The center position of a section.
### Serializing a section
- [func encode(to: any Encoder) throws](./section/encode%28to%29.md)
  Serializes a section to the specified encoder.

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
- [CapturedRoom.Confidence](./confidence.md)
  Levels of certainty in the classification of a particular detail in a scan.
- [var version: Int](./version.md)
  A version number for the captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/section)*