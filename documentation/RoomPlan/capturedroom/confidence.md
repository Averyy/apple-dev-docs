# CapturedRoom.Confidence

**Framework**: RoomPlan  
**Kind**: enum

Levels of certainty in the classification of a particular detail in a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Confidence
```

#### Overview

The framework chooses a level of certainty in its assessment of particular room features, such as:

- The [`confidence`](capturedroom/surface/confidence.md) in a [`category`](capturedroom/surface/category-swift.property.md) that the captured room assigns its surfaces, such as [`doors`](capturedroom/doors.md), [`openings`](capturedroom/openings.md), [`walls`](capturedroom/walls.md), [`windows`](capturedroom/windows.md).
- The [`confidence`](capturedroom/object/confidence.md) in a [`category`](capturedroom/object/category-swift.property.md) that the captured room assigns its [`objects`](capturedroom/objects.md).

## Topics

### Creating a confidence value
- [init(from: any Decoder) throws](capturedroom/confidence/init(from:).md)
  Creates a confidence value by deserializing the specified decoder.
### Assessing a confidence value
- [CapturedRoom.Confidence.high](capturedroom/confidence/high.md)
  A confidence value that represents a high level of certainty.
- [CapturedRoom.Confidence.medium](capturedroom/confidence/medium.md)
  A confidence value that represents a medium level of certainty.
- [CapturedRoom.Confidence.low](capturedroom/confidence/low.md)
  A confidence value that represents a low level of certainty.
### Comparing confidence values
- [static func == (CapturedRoom.Confidence, CapturedRoom.Confidence) -> Bool](capturedroom/confidence/==(_:_:).md)
  Determines whether two confidence values are equal.
- [static func != (Self, Self) -> Bool](capturedroom/confidence/!=(_:_:).md)
  Determines whether two confidence values aren’t equal.
- [func hash(into: inout Hasher)](capturedroom/confidence/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](capturedroom/confidence/hashvalue.md)
  The hash value.
### Serializing a confidence value
- [func encode(to: any Encoder) throws](capturedroom/confidence/encode(to:).md)
  Serializes a confidence value to the specified encoder.
### Default Implementations
- [Equatable Implementations](capturedroom/confidence/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [var version: Int](capturedroom/version.md)
  A version number for the captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/confidence)*