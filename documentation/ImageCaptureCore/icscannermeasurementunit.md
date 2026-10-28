# ICScannerMeasurementUnit

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

The unit of measurement used by the scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
enum ICScannerMeasurementUnit
```

```c
enum ICScannerMeasurementUnit : NSUInteger;
```

## Overview

The values correspond to the `ICAP_UNITS` values as defined in the `TWAIN` Specification.

## Topics

### Constants
- [ICScannerMeasurementUnit.centimeters](./icscannermeasurementunit/centimeters.md)
- [ICScannerMeasurementUnit.inches](./icscannermeasurementunit/inches.md)
- [ICScannerMeasurementUnit.picas](./icscannermeasurementunit/picas.md)
- [ICScannerMeasurementUnit.pixels](./icscannermeasurementunit/pixels.md)
- [ICScannerMeasurementUnit.points](./icscannermeasurementunit/points.md)
- [ICScannerMeasurementUnit.twips](./icscannermeasurementunit/twips.md)
### Initializers
- [init?(rawValue: UInt)](./icscannermeasurementunit/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Document Sizes
- [enum ICScannerDocumentType](./icscannerdocumenttype.md)
  The supported document size types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannermeasurementunit)*