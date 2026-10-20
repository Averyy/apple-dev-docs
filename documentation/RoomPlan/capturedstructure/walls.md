# walls

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

An array of all the walls in the structure.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var walls: [CapturedStructure.Surface] { get }
```

## See Also

### Inspecting structure details
- [var identifier: UUID](./identifier.md)
  A unique alphanumeric value that the framework assigns the structure.
- [var rooms: [CapturedRoom]](./rooms.md)
  An array of all the captured rooms in the structure.
- [var floors: [CapturedStructure.Surface]](./floors.md)
  An array of all the floors in the structure.
- [CapturedStructure.Surface](./surface.md)
  The type a captured structure assigns to surfaces.
- [var doors: [CapturedStructure.Surface]](./doors.md)
  An array of all the doors in the structure.
- [var objects: [CapturedStructure.Object]](./objects.md)
  An array of all the objects in the structure.
- [CapturedStructure.Object](./object.md)
  The type a captured structure assigns to objects.
- [var openings: [CapturedStructure.Surface]](./openings.md)
  An array of all the openings in the structure.
- [var windows: [CapturedStructure.Surface]](./windows.md)
  An array of all the windows in the structure.
- [var sections: [CapturedStructure.Section]](./sections.md)
  One or more room types that the framework identifies in the structure.
- [CapturedStructure.Section](./section.md)
  The type a captured structure assigns to distinct room areas.
- [var version: Int](./version.md)
  A version number for the captured structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedstructure/walls)*