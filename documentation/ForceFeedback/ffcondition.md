# FFCONDITION

**Framework**: Force Feedback  
**Kind**: struct

A structure containing type-specific information for certain effects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFCONDITION
```

#### Overview

Used with the SPRING, DAMPER, INERTIA, and FRICTION effects.A pointer to an array of FFCONDITION structures for an effect is passed in the  member of the FFEFFECT structure. The number of elements in the array must be either one, or equal to the number of axes associated with the effect.

Different types of conditions interpret the parameters differently, but the basic idea is that force resulting from a condition is equal to  where  is a scaling coefficient,  is some metric, and  is the neutral value for that metric.

The preceding simplified formula must be adjusted if a nonzero deadband is provided. If the metric is less than , the resulting force is given by the following formula:

 =  * ( - ())

Similarly, if the metric is greater than , the resulting force is given by the following formula:

 =  * ( - ())

A spring condition uses axis position as the metric.

A damper condition uses axis velocity as the metric.

An inertia condition uses axis acceleration as the metric.

If the number of FFCONDITION structures in the array is equal to the number of axes for the effect, the first structure applies to the first axis, the second applies to the second axis, and so on. For example, a two-axis spring condition with  set to 0 in both FFCONDITION structures would have the same effect as the joystick self-centering spring. When a condition is defined for each axis in this way, the effect must not be rotated.

If there is a single FFCONDITION structure for an effect with more than one axis, the direction along which the parameters of the FFCONDITION structure are in effect is determined by the direction parameters passed in the  field of the FFEFFECT structure. For example, a friction condition rotated 45 degrees (in polar coordinates) would resist joystick motion in the northeast-southwest direction but would have no effect on joystick motion in the northwest-southeast direction.

## Topics

### Initializers
- [init()](ffcondition/init.md)
- [init(lOffset: LONG, lPositiveCoefficient: LONG, lNegativeCoefficient: LONG, dwPositiveSaturation: DWORD, dwNegativeSaturation: DWORD, lDeadBand: LONG)](ffcondition/init(loffset:lpositivecoefficient:lnegativecoefficient:dwpositivesaturation:dwnegativesaturation:ldeadband:).md)
### Instance Properties
- [var dwNegativeSaturation: DWORD](ffcondition/dwnegativesaturation.md)
  Maximum force output on the negative side of the offset, in the range from 0 through 10,000.
- [var dwPositiveSaturation: DWORD](ffcondition/dwpositivesaturation.md)
  Maximum force output on the positive side of the offset, in the range from 0 through 10,000.
- [var lDeadBand: LONG](ffcondition/ldeadband.md)
  Region around  in which the condition is not active, in the range from 0 through 10,000. In other words, the condition is not active between  minus  and  plus .
- [var lNegativeCoefficient: LONG](ffcondition/lnegativecoefficient.md)
  Coefficient constant on the negative side of the offset, in the range from -10,000 through 10,000.
- [var lOffset: LONG](ffcondition/loffset.md)
  Offset for the condition, in the range from -10,000 through 10,000.
- [var lPositiveCoefficient: LONG](ffcondition/lpositivecoefficient.md)
  Coefficient constant on the positive side of the offset, in the range from -10,000 through 10,000.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct FFCAPABILITIES](ffcapabilities.md)
  Used by the FFDeviceGetForceFeedbackCapabilities method to retrieve device force-feedback capabilities.
- [struct FFCONSTANTFORCE](ffconstantforce.md)
  Contains type-specific information for the CONSTANTFORCE effect.
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

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcondition)*