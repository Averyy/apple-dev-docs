# FFEFFESCAPE

**Framework**: Force Feedback  
**Kind**: struct

The FFEFFESCAPE structure passes hardware-specific data directly to the Force Feedback plugIn.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct FFEFFESCAPE
```

## Topics

### Initializers
- [init()](ffeffescape/init.md)
- [init(dwSize: DWORD, dwCommand: DWORD, lpvInBuffer: UnsafeMutableRawPointer!, cbInBuffer: DWORD, lpvOutBuffer: UnsafeMutableRawPointer!, cbOutBuffer: DWORD)](ffeffescape/init(dwsize:dwcommand:lpvinbuffer:cbinbuffer:lpvoutbuffer:cboutbuffer:).md)
### Instance Properties
- [var cbInBuffer: DWORD](ffeffescape/cbinbuffer.md)
  Specifies the size, in bytes, of the  buffer.
- [var cbOutBuffer: DWORD](ffeffescape/cboutbuffer.md)
  On entry, specifies the size, in bytes, of the  buffer. On exit, specifies the number of bytes actually produced by the command.
- [var dwCommand: DWORD](ffeffescape/dwcommand.md)
  Specifies a plugIn specific command number. Contact the hardware vendor for a list of valid commands and their parameters.
- [var dwSize: DWORD](ffeffescape/dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.
- [var lpvInBuffer: UnsafeMutableRawPointer!](ffeffescape/lpvinbuffer.md)
  Buffer containing the data required to perform the operation.
- [var lpvOutBuffer: UnsafeMutableRawPointer!](ffeffescape/lpvoutbuffer.md)
  Buffer in which the operation’s output data is returned.

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
- [struct FFEFFECT](ffeffect.md)
  UsUsed by the FFDeviceCreateEffect method to initialize a new effect object. It is also used by the FFEffectSetParameters and FFEffectGetParameters functions.
- [struct FFENVELOPE](ffenvelope.md)
  Used by the FFEFFECT structure to specify the optional envelope parameters for an effect.
- [struct FFPERIODIC](ffperiodic.md)
  A structure containing type-specific information for certain effects.
- [struct FFRAMPFORCE](fframpforce.md)
  Contains type-specific information for the RAMPFORCE effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffescape)*