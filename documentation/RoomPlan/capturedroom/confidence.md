# CapturedRoom.Confidence

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

Levels of certainty in the classification of a particular detail in a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Confidence
```

## Overview

The framework chooses a level of certainty in its assessment of particular room features, such as:

- The [`confidence`](./surface/confidence.md) in a [`category`](./surface/category-swift.property.md) that the captured room assigns its surfaces, such as [`doors`](./doors.md), [`openings`](./openings.md), [`walls`](./walls.md), [`windows`](./windows.md).
- The [`confidence`](./object/confidence.md) in a [`category`](./object/category-swift.property.md) that the captured room assigns its [`objects`](./objects.md).

## Topics

### Assessing a confidence value
- [CapturedRoom.Confidence.high](./confidence/high.md)
  A confidence value that represents a high level of certainty.
- [CapturedRoom.Confidence.medium](./confidence/medium.md)
  A confidence value that represents a medium level of certainty.
- [CapturedRoom.Confidence.low](./confidence/low.md)
  A confidence value that represents a low level of certainty.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
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
- [CapturedRoom.Section](./section.md)
  An object that identifies a particular area in a captured room in relation to common types of room areas in a building.
- [var version: Int](./version.md)
  A version number for the captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/confidence)*