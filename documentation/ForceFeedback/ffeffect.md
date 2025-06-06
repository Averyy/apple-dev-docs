# FFEFFECT

**Framework**: Force Feedback  
**Kind**: struct

UsUsed by the FFDeviceCreateEffect method to initialize a new effect object. It is also used by the FFEffectSetParameters and FFEffectGetParameters functions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFEFFECT
```

#### Overview

OBJECT IDS cannot be used to identify trigger buttons in , and output axes in . Please use object offsets (FFJOFS_* constants), the only supported method.

## Topics

### Initializers
- [init()](ffeffect/init.md)
- [init(dwSize: DWORD, dwFlags: DWORD, dwDuration: DWORD, dwSamplePeriod: DWORD, dwGain: DWORD, dwTriggerButton: DWORD, dwTriggerRepeatInterval: DWORD, cAxes: DWORD, rgdwAxes: LPDWORD!, rglDirection: LPLONG!, lpEnvelope: PFFENVELOPE!, cbTypeSpecificParams: DWORD, lpvTypeSpecificParams: UnsafeMutableRawPointer!, dwStartDelay: DWORD)](ffeffect/init(dwsize:dwflags:dwduration:dwsampleperiod:dwgain:dwtriggerbutton:dwtriggerrepeatinterval:caxes:rgdwaxes:rgldirection:lpenvelope:cbtypespecificparams:lpvtypespecificparams:dwstartdelay:).md)
### Instance Properties
- [var cAxes: DWORD](ffeffect/caxes.md)
  Number of axes involved in the effect.
- [var cbTypeSpecificParams: DWORD](ffeffect/cbtypespecificparams.md)
  Number of bytes of additional type-specific parameters for the corresponding effect type.
- [var dwDuration: DWORD](ffeffect/dwduration.md)
  The total duration of the effect, in microseconds. If this value is FF_INFINITE, the effect has infinite duration. If an envelope has been applied to the effect, the attack is applied, followed by an infinite sustain.
- [var dwFlags: DWORD](ffeffect/dwflags.md)
  Flags associated with an effect.
- [var dwGain: DWORD](ffeffect/dwgain.md)
  The gain to be applied to the effect, in the range from 0 through 10,000. The gain is a scaling factor applied to all magnitudes of the effect and its envelope.
- [var dwSamplePeriod: DWORD](ffeffect/dwsampleperiod.md)
  The period at which the device should play back the effect, in microseconds.
- [var dwSize: DWORD](ffeffect/dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.
- [var dwStartDelay: DWORD](ffeffect/dwstartdelay.md)
  Time (in microseconds) that the device should wait after a FFEffectStart call before playing the effect. If this value is 0, effect playback begins immediately.
- [var dwTriggerButton: DWORD](ffeffect/dwtriggerbutton.md)
  The identifier or offset of the button to be used to trigger playback of the effect. The FFJOFS_* flags must be used to specify the value. If this member is set to FFEB_NOTRIGGER, no trigger button is associated with the effect.
- [var dwTriggerRepeatInterval: DWORD](ffeffect/dwtriggerrepeatinterval.md)
  The interval, in microseconds, between the end of one playback and the start of the next when the effect is triggered by a button press and the button is held down. Setting this value to FF_INFINITE suppresses repetition.
- [var lpEnvelope: PFFENVELOPE!](ffeffect/lpenvelope.md)
  Optional pointer to a FFENVELOPE structure that describes the envelope to be used by this effect. Not all effect types use envelopes. If no envelope is to be applied, the member should be set to NULL.
- [var lpvTypeSpecificParams: UnsafeMutableRawPointer!](ffeffect/lpvtypespecificparams.md)
  A pointer to type-specific parameters, or NULL if there are no type-specific parameters.
- [var rgdwAxes: LPDWORD!](ffeffect/rgdwaxes.md)
  Pointer to a DWORD array (of  elements) containing identifiers or offsets identifying the axes to which the effect is to be applied.
- [var rglDirection: LPLONG!](ffeffect/rgldirection.md)
  Pointer to a LONG array (of  elements) containing either Cartesian coordinates, polar coordinates, or spherical coordinates.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct FFCAPABILITIES](ffcapabilities.md)
  Used by the FFDeviceGetForceFeedbackCapabilities method to retrieve device force-feedback capabilities.
- [struct FFCONDITION](ffcondition.md)
  A structure containing type-specific information for certain effects.
- [struct FFCONSTANTFORCE](ffconstantforce.md)
  Contains type-specific information for the CONSTANTFORCE effect.
- [struct FFCUSTOMFORCE](ffcustomforce.md)
  Contains type-specific information for the CUSTOMFORCE effect.
- [struct FFEFFESCAPE](ffeffescape.md)
  The FFEFFESCAPE structure passes hardware-specific data directly to the Force Feedback plugIn.
- [struct FFENVELOPE](ffenvelope.md)
  Used by the FFEFFECT structure to specify the optional envelope parameters for an effect.
- [struct FFPERIODIC](ffperiodic.md)
  A structure containing type-specific information for certain effects.
- [struct FFRAMPFORCE](fframpforce.md)
  Contains type-specific information for the RAMPFORCE effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffect)*