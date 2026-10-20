# FFRAMPFORCE

**Framework**: Force Feedback  
**Kind**: struct  
**Role**: Structure

Contains type-specific information for the RAMPFORCE effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFRAMPFORCE
```

```c
struct FFRAMPFORCE;
```

#### Overview

A pointer to a single FFRAMPFORCE structure for an effect is passed in the **lpvTypeSpecificParams** member of the FFEFFECT structure.

The dwDuration for a ramp force effect cannot be FF_INFINITE.

## Topics

### Initializers
- [init()](./fframpforce/init%28%29.md)
- [init(lStart: LONG, lEnd: LONG)](./fframpforce/init%28lstart,lend%29.md)
### Instance Properties
- [var lEnd: LONG](./fframpforce/lend.md)
  Magnitude at the end of the effect, in the range from -10,000 through 10,000.
- [var lStart: LONG](./fframpforce/lstart.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [struct FFCAPABILITIES](./ffcapabilities.md)
  Used by the FFDeviceGetForceFeedbackCapabilities method to retrieve device force-feedback capabilities.
- [struct FFCONDITION](./ffcondition.md)
  A structure containing type-specific information for certain effects.
- [struct FFCONSTANTFORCE](./ffconstantforce.md)
  Contains type-specific information for the CONSTANTFORCE effect.
- [struct FFCUSTOMFORCE](./ffcustomforce.md)
  Contains type-specific information for the CUSTOMFORCE effect.
- [struct FFEFFECT](./ffeffect.md)
  UsUsed by the FFDeviceCreateEffect method to initialize a new effect object. It is also used by the FFEffectSetParameters and FFEffectGetParameters functions.
- [struct FFEFFESCAPE](./ffeffescape.md)
  The FFEFFESCAPE structure passes hardware-specific data directly to the Force Feedback plugIn.
- [struct FFENVELOPE](./ffenvelope.md)
  Used by the FFEFFECT structure to specify the optional envelope parameters for an effect.
- [struct FFPERIODIC](./ffperiodic.md)
  A structure containing type-specific information for certain effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/fframpforce)*