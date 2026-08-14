# CapturedElementCategory

**Framework**: RoomPlan  
**Kind**: enum

The category of the particular object or surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum CapturedElementCategory
```

#### Overview

A  [`CapturedRoomAttribute`](capturedroomattribute.md) adopter’s [`parentCategory`](capturedroomattribute/parentcategory.md) property is of this type.

## Topics

### Determining the category type
- [case object(CapturedRoom.Object.Category)](capturedelementcategory/object(_:).md)
  A category that’s scoped to the captured object.
- [case surface(CapturedRoom.Surface.Category)](capturedelementcategory/surface(_:).md)
  A category that’s scoped to the captured surface.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol CapturedRoomAttribute](capturedroomattribute.md)
  Details about an object in the room that the framework observes during a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedelementcategory)*