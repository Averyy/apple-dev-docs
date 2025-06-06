# CapturedRoomAttribute

**Framework**: RoomPlan  
**Kind**: protocol

Details about an object in the room that the framework observes during a scan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
protocol CapturedRoomAttribute : CaseIterable, RawRepresentable, Sendable where Self.RawValue == String
```

#### Overview

If the framework identifies details about an [`CapturedRoom.Object`](capturedroom/object.md) during a scan, it adds an adopter of this protocol that represents that detail to the object’s [`attributes`](capturedroom/object/attributes.md) array. For example, details the framework recognizes as a stool with a star-shaped base contains both of the [`ChairType.stool`](chairtype/stool.md) and [`ChairLegType.star`](chairlegtype/star.md) options in the `attributes` array for the object that represents the physical stool.

## Topics

### Identifying an attribute
- [var shortIdentifier: String](capturedroomattribute/shortidentifier.md)
  A human-readable identifier for the attribute.
### Determining an attribute’s category
- [static var parentCategory: CapturedElementCategory?](capturedroomattribute/parentcategory.md)
  A category to which this room attribute belongs.

## Relationships

### Inherits From
- [CaseIterable](../Swift/CaseIterable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [ChairArmType](chairarmtype.md)
- [ChairBackType](chairbacktype.md)
- [ChairLegType](chairlegtype.md)
- [ChairType](chairtype.md)
- [SofaType](sofatype.md)
- [StorageType](storagetype.md)
- [TableShapeType](tableshapetype.md)
- [TableType](tabletype.md)

## See Also

- [enum CapturedElementCategory](capturedelementcategory.md)
  The category of the particular object or surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroomattribute)*