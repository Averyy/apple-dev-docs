# StartEffect

**Framework**: Force Feedback  
**Role**: Article

This function commands the device to play back an effect that was previously loaded.

#### Overview

```c
HRESULT ( *StartEffect)(
   void *self,
   FFEffectDownloadID downloadID,
   FFEffectStartFlag mode,
   UInt32 iterations );
```

##### Parameters

- **self**: Pointer to the FFPlugInDriver implementation instance.
- **downloadID**: Indicates the effect to be played.
- **mode**: Specifies how the effect is to affect other effects. Only the mode listed below can be used; all other modes are reserved. For example, the driver never receives the FFES_NODOWNLOAD flag because it is managed by the FF API and not the PlugIn driver. This parameter can be zero, one, or more of the following flags:

  FFES_SOLO

  Indicates that all other effects on the device should be stopped before the specified effect is played. If this flag is omitted, the effect is mixed with existing effects that have already started on the device.
- **iterations**: Specifies the number of times to perform the effect. If the value is FF_INFINITE, then the effect should be repeated until explicitly stopped or paused.

##### Return Value

Returns FF_OK if successful, or an error value otherwise:

FFERR_INTERNAL

FFERR_DEVICEPAUSED

FFERR_DEVICEFULL

FFERR_GENERIC

FFERR_INVALIDDOWNLOADID

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
- [SetProperty](./setproperty.md)
  This function sets properties that define the device behavior.
- [StopEffect](./stopeffect.md)
  This function commands the device to stop an effect that was previously started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/starteffect)*