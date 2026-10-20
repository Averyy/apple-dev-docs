# Accessory.LocationName

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Location names to fetch transforms defined on accessories. Some pre-defined location names that are common to accessories conforming to the OpenXR spec are provided as a convenience. These are not required to exist on all accessories.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct LocationName
```

## Topics

### Initializers
- [init(String)](./locationname/init%28_%29.md)
  Init without label provided as a convenience.
- [init(rawValue: String)](./locationname/init%28rawvalue%29.md)
  Init with label (required by RawRepresentable).
### Instance Properties
- [var description: String](./locationname/description.md)
  Textual representation of this location name.
- [let rawValue: String](./locationname/rawvalue.md)
  The location name string.
### Type Properties
- [static let aim: Accessory.LocationName](./locationname/aim.md)
  Aim point for spatial gamepads and styluses.
- [static let grip: Accessory.LocationName](./locationname/grip.md)
  Grip for spatial gamepads.
- [static let gripSurface: Accessory.LocationName](./locationname/gripsurface.md)
  Grip surface for spatial gamepads.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessory/locationname)*