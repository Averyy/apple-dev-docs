# doors

**Framework**: RoomPlan  
**Kind**: property

An array of doors that the framework identifies during a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var doors: [CapturedRoom.Surface] { get }
```

## See Also

- [var identifier: UUID](capturedroom/identifier.md)
  A unique alphanumeric value that the framework assigns the room.
- [var story: Int](capturedroom/story.md)
  The story, floor number, or level on which the captured room resides within a larger structure.
- [var floors: [CapturedRoom.Surface]](capturedroom/floors.md)
  An array of floors that the framework identifies during a scan.
- [CapturedRoom.Surface](capturedroom/surface.md)
  A 2D area in a room that the framework identifies as a surface.
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

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/doors)*