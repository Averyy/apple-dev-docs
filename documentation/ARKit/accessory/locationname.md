# Accessory.LocationName

**Framework**: ARKit  
**Kind**: struct

Location names to fetch transforms defined on accessories. Some pre-defined location names that are common to accessories conforming to the OpenXR spec are provided as a convenience. These are not required to exist on all accessories.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct LocationName
```

## Topics

### Initializers
- [init(String)](accessory/locationname/init(_:).md)
  Init without label provided as a convenience.
- [init(rawValue: String)](accessory/locationname/init(rawvalue:).md)
  Init with label (required by RawRepresentable).
### Instance Properties
- [var description: String](accessory/locationname/description.md)
  Textual representation of this location name.
- [let rawValue: String](accessory/locationname/rawvalue.md)
  The location name string.
### Type Properties
- [static let aim: Accessory.LocationName](accessory/locationname/aim.md)
  Aim point for spatial gamepads and styluses.
- [static let grip: Accessory.LocationName](accessory/locationname/grip.md)
  Grip for spatial gamepads.
- [static let gripSurface: Accessory.LocationName](accessory/locationname/gripsurface.md)
  Grip surface for spatial gamepads.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessory/locationname)*