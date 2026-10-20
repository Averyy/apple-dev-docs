# identifier

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

A unique alphanumeric value that the framework assigns the object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var identifier: UUID { get }
```

## See Also

### Identifying an object
- [var parentIdentifier: UUID?](./parentidentifier.md)
  A unique alphanumeric value that identifies the object’s parent object or surface.
- [var category: CapturedRoom.Object.Category](./category-swift.property.md)
  A classification that the captured room assigns the object.
- [CapturedRoom.Object.Category](./category-swift.enum.md)
  Classifications of an object in a captured room.
- [var confidence: CapturedRoom.Confidence](./confidence.md)
  A level of certainty in the object’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object/identifier)*