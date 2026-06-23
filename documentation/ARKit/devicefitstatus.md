# DeviceFitStatus

**Framework**: ARKit  
**Kind**: enum

Device fit validation status indicating the user’s eye position relative to the optimal device fit range.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum DeviceFitStatus
```

## Topics

### Enumeration Cases
- [DeviceFitStatus.eyesAbove](devicefitstatus/eyesabove.md)
  User’s eyes are positioned above the optimal device fit range.
- [DeviceFitStatus.eyesBelow](devicefitstatus/eyesbelow.md)
  User’s eyes are positioned below the optimal device fit range.
- [DeviceFitStatus.eyesLeft](devicefitstatus/eyesleft.md)
  User’s eyes are positioned to the left of the optimal device fit range.
- [DeviceFitStatus.eyesRight](devicefitstatus/eyesright.md)
  User’s eyes are positioned to the right of the optimal device fit range.
- [DeviceFitStatus.valid](devicefitstatus/valid.md)
  User’s eyes are properly positioned within the optimal device fit range.
### Instance Properties
- [var description: String](devicefitstatus/description.md)
  A textual representation of the device fit status.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class VisualFidelityProvider](visualfidelityprovider.md)
  A data provider that delivers visual fidelity monitoring data.
- [struct VisualFidelityData](visualfidelitydata.md)
  Visual fidelity data containing device fit and field of view verification.
- [struct FieldOfViewAnchor](fieldofviewanchor.md)
  An anchor representing a set of field of view (FoV) boundary polygon points in immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/devicefitstatus)*