# SetProperty

**Framework**: Force Feedback  
**Role**: Article

This function sets properties that define the device behavior.

## Overview

```c
HRESULT ( *SetProperty)(
   void *self,
   FFProperty property,
   void *pValue );
```

### Parameters

- **self**: Pointer to the FFPlugInDriver implementation instance.
- **property**: The following property values are defined for a FF device:

  FFPROP_AUTOCENTER

  Specifies whether the actuated FF axes are self-centering. This property controls the devicexD5s xD2default centering springxD3.

  The pValue member points to a UInt32 and can be one of the following values.

  0 - OFF: The device should not automatically center when the user releases the device. An application that uses force feedback should disable autocentering before playing effects.

  1 - ON: The device should automatically center when the user releases the device.

  Not all devices support the autocenter property.

  FFPROP_FFGAIN

  Sets the gain for the device.

  The pValue member points to a UInt32 that contains a gain value that is applied to all effects created on the device. The value is an integer in the range from 0 through 10,000, specifying the amount by which effect magnitudes should be scaled for the device. For example, a value of 10,000 indicates that all effect magnitudes are to be taken at face value. A value of 9,000 indicates that all effect magnitudes are to be reduced to 90% of their nominal magnitudes.

  Setting a gain value is useful when an application wants to scale down the strength of all force-feedback effects uniformly, based on user preferences.
- **pValue**: Address of the location where the property value is to be read. This function will assume that the data is valid, and of the correct type.

### Return Value

If the method succeeds, the return value is FF_OK or FFERR_UNSUPPORTED. If the method fails, the return value can be one of the following error values:

FFERR_INVALIDPARAM

## See Also

### Miscellaneous
- [DestroyEffect](./destroyeffect.md)
  This function commands the device to “destroy” a currently downloaded effect. The effect ID and any data that is associated with the effect are freed and available for reallocation.
- [DownloadEffect](./downloadeffect.md)
  This function sends an effect to the device.
- [Escape](./escape.md)
  This function escapes to the driver. This method is called in response to an application invoking the FFEffectEscape or FFDeviceEscape methods.
- [ForceFeedbackGetVersion](./forcefeedbackgetversion.md)
  This function is used to determine driver and API version information.
- [GetEffectStatus](./geteffectstatus.md)
  This function returns the device effect’s status.
- [GetForceFeedbackCapabilities](./getforcefeedbackcapabilities.md)
  This function escapes to the driver. This method is called in response to an application invoking the FFEffectEscape or FFDevicEscape methods.
- [GetForceFeedbackState](./getforcefeedbackstate.md)
  This function returns the state of the device.
- [InitializeTerminate](./initializeterminate.md)
  This function is used to “create and destroy” particular device instances. It provides the FF plug-in driver with all the necessary start-up parameters.
- [SendForceFeedbackCommand](./sendforcefeedbackcommand.md)
  This function sends a command to the device.
- [StartEffect](./starteffect.md)
  This function commands the device to play back an effect that was previously loaded.
- [StopEffect](./stopeffect.md)
  This function commands the device to stop an effect that was previously started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/setproperty)*