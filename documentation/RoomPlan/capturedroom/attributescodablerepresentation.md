# CapturedRoom.AttributesCodableRepresentation

**Framework**: RoomPlan  
**Kind**: struct

A serializable set of details that describe an object in the room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct AttributesCodableRepresentation
```

#### Overview

}

## Topics

### Creating an attributes codable representation
- [init(from: any Decoder) throws](capturedroom/attributescodablerepresentation/init(from:).md)
  Deserializes an attributes codable representation from the given decoder.
- [init(attributes: [any CapturedRoomAttribute])](capturedroom/attributescodablerepresentation/init(attributes:).md)
  Creates an attributes codable representation with the given collection of object attributes.
### Accessing room attributes
- [let attributes: [any CapturedRoomAttribute]](capturedroom/attributescodablerepresentation/attributes.md)
  A collection of object attributes.
### Serializing an attributes codable representation
- [func encode(to: any Encoder) throws](capturedroom/attributescodablerepresentation/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [func encode(to: any Encoder) throws](capturedroom/encode(to:).md)
  Serializes a captured room to the specified encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/attributescodablerepresentation)*