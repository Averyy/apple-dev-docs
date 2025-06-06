# FFCUSTOMFORCE

**Framework**: Force Feedback  
**Kind**: struct

Contains type-specific information for the CUSTOMFORCE effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFCUSTOMFORCE
```

#### Overview

A pointer to a single FFCUSTOMFORCE structure for an effect is passed in the  member of the FFEFFECT structure.

The structure describes a custom or user-defined force.

## Topics

### Initializers
- [init()](ffcustomforce/init.md)
- [init(cChannels: DWORD, dwSamplePeriod: DWORD, cSamples: DWORD, rglForceData: LPLONG!)](ffcustomforce/init(cchannels:dwsampleperiod:csamples:rglforcedata:).md)
### Instance Properties
- [var cChannels: DWORD](ffcustomforce/cchannels.md)
  Number of channels (axes) affected by this force.
- [var cSamples: DWORD](ffcustomforce/csamples.md)
  Total number of samples in the . It must be an integral multiple of the .
- [var dwSamplePeriod: DWORD](ffcustomforce/dwsampleperiod.md)
  Sample period, in microseconds.
- [var rglForceData: LPLONG!](ffcustomforce/rglforcedata.md)
  Pointer to an array of force values representing the custom force. If multiple channels are provided, the values are interleaved. For example, if  is 3, the first element of the array belongs to the first channel, the second to the second, and the third to the third.

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

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcustomforce)*