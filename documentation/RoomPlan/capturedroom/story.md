# story

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

The story, floor number, or level on which the captured room resides within a larger structure.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var story: Int { get }
```

## See Also

### Inspecting room details
- [var identifier: UUID](./identifier.md)
  A unique alphanumeric value that the framework assigns the room.
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
- [CapturedRoom.Confidence](./confidence.md)
  Levels of certainty in the classification of a particular detail in a scan.
- [var version: Int](./version.md)
  A version number for the captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/story)*