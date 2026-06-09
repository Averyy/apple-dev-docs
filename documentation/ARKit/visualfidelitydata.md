# VisualFidelityData

**Framework**: ARKit  
**Kind**: struct

Visual fidelity data containing device fit and field of view verification.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VisualFidelityData
```

## Topics

### Operators
- [static func == (VisualFidelityData, VisualFidelityData) -> Bool](visualfidelitydata/==(_:_:).md)
  Compares two visual fidelity data instances for equality.
### Instance Properties
- [var description: String](visualfidelitydata/description.md)
  A textual representation of this visual fidelity data.
- [var deviceFitStatus: DeviceFitStatus](visualfidelitydata/devicefitstatus.md)
  The device fit validation status.
- [var isFieldOfViewValid: Bool](visualfidelitydata/isfieldofviewvalid.md)
  Indicates whether the field of view (FoV) is valid.
- [var timestamp: TimeInterval](visualfidelitydata/timestamp.md)
  The timestamp when this validation data was captured.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class VisualFidelityProvider](visualfidelityprovider.md)
  A data provider that delivers visual fidelity monitoring data.
- [struct FieldOfViewAnchor](fieldofviewanchor.md)
  An anchor representing a set of field of view (FoV) boundary polygon points in immersive space.
- [enum DeviceFitStatus](devicefitstatus.md)
  Device fit validation status indicating the user’s eye position relative to the optimal device fit range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelitydata)*