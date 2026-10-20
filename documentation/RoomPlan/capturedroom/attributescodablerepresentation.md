# CapturedRoom.AttributesCodableRepresentation

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

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
- [init(from: any Decoder) throws](./attributescodablerepresentation/init%28from%29.md)
  Deserializes an attributes codable representation from the given decoder.
- [init(attributes: [any CapturedRoomAttribute])](./attributescodablerepresentation/init%28attributes%29.md)
  Creates an attributes codable representation with the given collection of object attributes.
### Accessing room attributes
- [let attributes: [any CapturedRoomAttribute]](./attributescodablerepresentation/attributes.md)
  A collection of object attributes.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)

## See Also

### Serializing a captured room
- [func encode(to: any Encoder) throws](./encode%28to%29.md)
  Serializes a captured room to the specified encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/attributescodablerepresentation)*