# lpvTypeSpecificParams

**Framework**: Force Feedback  
**Kind**: property

A pointer to type-specific parameters, or NULL if there are no type-specific parameters.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var lpvTypeSpecificParams: UnsafeMutableRawPointer!
```

#### Discussion

If the effect is of type FFEFT_CONDITION, this member contains a pointer to an array of FFCONDITION structures that define the parameters for the condition. A single structure may be used, in which case the condition is applied in the direction specified in the rglDirection array. Otherwise, there must be one structure for each axis, in the same order as the axes in rgdwAxes array. If a structure is supplied for each axis, the effect should not be rotated; you should use the following values in the rglDirection array:

FFEFF_SPHERICAL: 0, 0, …

FFEFF_POLAR: 9000, 0, …

FFEFF_CARTESIAN: 1, 0, …

If the effect is of type FFEFT_CUSTOMFORCE, this member contains a pointer to a FFCUSTOMFORCE structure that defines the parameters for the custom force.

If the effect is of type FFEFT_PERIODIC, this member contains a pointer to a FFPERIODIC structure that defines the parameters for the effect.

If the effect is of type FFEFT_CONSTANTFORCE, this member contains a pointer to a FFCONSTANTFORCE structure that defines the parameters for the constant force.

If the effect is of type FFEFT_RAMPFORCE, this member contains a pointer to a FFRAMPFORCE structure that defines the parameters for the ramp force.

## See Also

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
- [var rgdwAxes: LPDWORD!](ffeffect/rgdwaxes.md)
  Pointer to a DWORD array (of  elements) containing identifiers or offsets identifying the axes to which the effect is to be applied.
- [var rglDirection: LPLONG!](ffeffect/rgldirection.md)
  Pointer to a LONG array (of  elements) containing either Cartesian coordinates, polar coordinates, or spherical coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffect/lpvtypespecificparams)*