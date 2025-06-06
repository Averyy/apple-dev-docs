# FFCONSTANTFORCE

**Framework**: Force Feedback  
**Kind**: struct

Contains type-specific information for the CONSTANTFORCE effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFCONSTANTFORCE
```

#### Overview

A pointer to a single FFCONSTANTFORCE structure for an effect is passed in the  member of the FFEFFECT structure.

## Topics

### Initializers
- [init()](ffconstantforce/init.md)
- [init(lMagnitude: LONG)](ffconstantforce/init(lmagnitude:).md)
### Instance Properties
- [var lMagnitude: LONG](ffconstantforce/lmagnitude.md)
  The magnitude of the effect, in the range from -10,000 through 10,000. If an envelope is applied to this effect, the value represents the magnitude of the sustain. If no envelope is applied, the value represents the amplitude of the entire effect.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct FFCAPABILITIES](ffcapabilities.md)
  Used by the FFDeviceGetForceFeedbackCapabilities method to retrieve device force-feedback capabilities.
- [struct FFCONDITION](ffcondition.md)
  A structure containing type-specific information for certain effects.
- [struct FFCUSTOMFORCE](ffcustomforce.md)
  Contains type-specific information for the CUSTOMFORCE effect.
- [struct FFEFFECT](ffeffect.md)
  UsUsed by the FFDeviceCreateEffect method to initialize a new effect object. It is also used by the FFEffectSetParameters and FFEffectGetParameters functions.
- [struct FFEFFESCAPE](ffeffescape.md)
  The FFEFFESCAPE structure passes hardware-specific data directly to the Force Feedback plugIn.
- [struct FFENVELOPE](ffenvelope.md)
  Used by the FFEFFECT structure to specify the optional envelope parameters for an effect.
- [struct FFPERIODIC](ffperiodic.md)
  A structure containing type-specific information for certain effects.
- [struct FFRAMPFORCE](fframpforce.md)
  Contains type-specific information for the RAMPFORCE effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffconstantforce)*