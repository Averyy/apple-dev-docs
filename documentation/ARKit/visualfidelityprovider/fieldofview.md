# VisualFidelityProvider.FieldOfView

**Framework**: ARKit  
**Kind**: struct

A field of view (FoV) specification.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FieldOfView
```

#### Overview

The preset FoVs are the recommended specification method for most applications. They provide standardized FoV requirements.

## Topics

### Instance Properties
- [var description: String](visualfidelityprovider/fieldofview/description.md)
  A textual representation of the field of view.
- [var isValid: Bool](visualfidelityprovider/fieldofview/isvalid.md)
  Validates whether this field of view specification is valid.
### Type Properties
- [static let presetA: VisualFidelityProvider.FieldOfView](visualfidelityprovider/fieldofview/preseta.md)
  Preset field of view A.
- [static let presetB: VisualFidelityProvider.FieldOfView](visualfidelityprovider/fieldofview/presetb.md)
  Preset field of view B.
- [static let presetC: VisualFidelityProvider.FieldOfView](visualfidelityprovider/fieldofview/presetc.md)
  Preset field of view C.
- [static let presetD: VisualFidelityProvider.FieldOfView](visualfidelityprovider/fieldofview/presetd.md)
  Preset field of view D.
### Type Methods
- [static func polygon(points: [simd_float2]) -> VisualFidelityProvider.FieldOfView](visualfidelityprovider/fieldofview/polygon(points:).md)
  Creates a polygon-based field of view.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelityprovider/fieldofview)*