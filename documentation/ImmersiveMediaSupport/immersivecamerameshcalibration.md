# ImmersiveCameraMeshCalibration

**Framework**: Immersive Media Support  
**Kind**: class

Calibration mesh geometry based on USDZ data.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class ImmersiveCameraMeshCalibration
```

#### Overview

This class is associated with the calibration type ‘usdzMesh’ and is used for calibration performed by camera lens provider using usdz.

## Topics

### Initializers
- [init(from: any Decoder) throws](immersivecamerameshcalibration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(name: String, usdzData: Data)](immersivecamerameshcalibration/init(name:usdzdata:).md)
  Creates an instance of `ImmersiveCameraMeshCalibration`.
### Instance Properties
- [let name: String](immersivecamerameshcalibration/name.md)
- [let usdzData: Data](immersivecamerameshcalibration/usdzdata.md)
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecamerameshcalibration/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamerameshcalibration)*