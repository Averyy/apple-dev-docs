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
### Creating a category
- [init(from: any Decoder) throws](capturedelementcategory/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (CapturedElementCategory, CapturedElementCategory) -> Bool](capturedelementcategory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](capturedelementcategory/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](capturedelementcategory/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CapturedRoomAttribute](capturedroomattribute.md)
  Details about an object in the room that the framework observes during a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedelementcategory)*