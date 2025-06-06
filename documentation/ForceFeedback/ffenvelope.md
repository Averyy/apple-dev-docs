# FFENVELOPE

**Framework**: Force Feedback  
**Kind**: struct

Used by the FFEFFECT structure to specify the optional envelope parameters for an effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFENVELOPE
```

#### Overview

The sustain level for the envelope is represented by the  member of the FFPERIODIC structure and the  member of the FFCONSTANTFORCE structure. The sustain time is represented by  member of the FFEFFECT structure

## Topics

### Initializers
- [init()](ffenvelope/init.md)
- [init(dwSize: DWORD, dwAttackLevel: DWORD, dwAttackTime: DWORD, dwFadeLevel: DWORD, dwFadeTime: DWORD)](ffenvelope/init(dwsize:dwattacklevel:dwattacktime:dwfadelevel:dwfadetime:).md)
### Instance Properties
- [var dwAttackLevel: DWORD](ffenvelope/dwattacklevel.md)
  Amplitude for the start of the envelope, relative to the baseline, in the range from 0 through 10,000. If the effect’s type-specific data does not specify a baseline, the amplitude is relative to 0.
- [var dwAttackTime: DWORD](ffenvelope/dwattacktime.md)
  The time, in microseconds, to reach the sustain level.
- [var dwFadeLevel: DWORD](ffenvelope/dwfadelevel.md)
  Amplitude for the end of the envelope, relative to the baseline, in the range from 0 through 10,000. If the effect’s type-specific data does not specify a baseline, the amplitude is relative to 0.
- [var dwFadeTime: DWORD](ffenvelope/dwfadetime.md)
  The time, in microseconds, to reach the fade level.
- [var dwSize: DWORD](ffenvelope/dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct FFCAPABILITIES](ffcapabilities.md)
  Used by the FFDeviceGetForceFeedbackCapabilities method to retrieve device force-feedback capabilities.
- [struct FFCONDITION](ffcondition.md)
  A structure containing type-specific information for certain effects.
- [struct FFCONSTANTFORCE](ffconstantforce.md)
  Contains type-specific information for the CONSTANTFORCE effect.
- [struct FFCUSTOMFORCE](ffcustomforce.md)
  Contains type-specific information for the CUSTOMFORCE effect.
- [struct FFEFFECT](ffeffect.md)
  UsUsed by the FFDeviceCreateEffect method to initialize a new effect object. It is also used by the FFEffectSetParameters and FFEffectGetParameters functions.
- [struct FFEFFESCAPE](ffeffescape.md)
  The FFEFFESCAPE structure passes hardware-specific data directly to the Force Feedback plugIn.
- [struct FFPERIODIC](ffperiodic.md)
  A structure containing type-specific information for certain effects.
- [struct FFRAMPFORCE](fframpforce.md)
  Contains type-specific information for the RAMPFORCE effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffenvelope)*