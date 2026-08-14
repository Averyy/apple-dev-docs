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
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessory/locationname)*