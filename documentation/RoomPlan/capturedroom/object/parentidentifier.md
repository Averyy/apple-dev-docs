# parentIdentifier

**Framework**: RoomPlan  
**Kind**: property

A unique alphanumeric value that identifies the object’s parent object or surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var parentIdentifier: UUID? { get }
```

#### Discussion

For example, the parent of a sink is the storage area in which the sink resides.

## See Also

- [var identifier: UUID](capturedroom/object/identifier.md)
  A unique alphanumeric value that the framework assigns the object.
- [var category: CapturedRoom.Object.Category](capturedroom/object/category-swift.property.md)
  A classification that the captured room assigns the object.
- [CapturedRoom.Object.Category](capturedroom/object/category-swift.enum.md)
  Classifications of an object in a captured room.
- [var confidence: CapturedRoom.Confidence](capturedroom/object/confidence.md)
  A level of certainty in the object’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object/parentidentifier)*