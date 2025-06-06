# ForceFeedbackDeviceState

**Framework**: Force Feedback  
**Kind**: struct

Returns information about the state of a force feedback device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
struct ForceFeedbackDeviceState;
```

## Topics

### Instance Properties
- [dwLoad](forcefeedbackdevicestate/dwload.md)
  A value indicating the percentage of device memory in use. A value of zero indicates that the device memory is completely available. A value of 100 indicates that the device is full
- [dwSize](forcefeedbackdevicestate/dwsize.md)
  Specifies the size of the structure in bytes. This member must be initialized before the structure is used.
- [dwState](forcefeedbackdevicestate/dwstate.md)
  Indicates various aspects of the device state.

## See Also

- [FFEffectDownloadID](ffeffectdownloadid.md)
  Unique identification for an effect.
- [ForceFeedbackVersion](forcefeedbackversion.md)
  Used to return plugIn version information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/forcefeedbackdevicestate)*