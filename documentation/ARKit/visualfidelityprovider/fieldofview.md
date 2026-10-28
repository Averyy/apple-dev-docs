# VisualFidelityProvider.FieldOfView

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A field of view (FoV) specification.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
struct FieldOfView
```

## Overview

The preset FoVs are the recommended specification method for most applications. They provide standardized FoV requirements.

## Topics

### Instance Properties
- [var description: String](./fieldofview/description.md)
  A textual representation of the field of view.
- [var isValid: Bool](./fieldofview/isvalid.md)
  Validates whether this field of view specification is valid.
### Type Properties
- [static let presetA: VisualFidelityProvider.FieldOfView](./fieldofview/preseta.md)
  Preset field of view A.
- [static let presetB: VisualFidelityProvider.FieldOfView](./fieldofview/presetb.md)
  Preset field of view B.
- [static let presetC: VisualFidelityProvider.FieldOfView](./fieldofview/presetc.md)
  Preset field of view C.
- [static let presetD: VisualFidelityProvider.FieldOfView](./fieldofview/presetd.md)
  Preset field of view D.
### Type Methods
- [static func polygon(points: [simd_float2]) -> VisualFidelityProvider.FieldOfView](./fieldofview/polygon%28points%29.md)
  Creates a polygon-based field of view.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelityprovider/fieldofview)*