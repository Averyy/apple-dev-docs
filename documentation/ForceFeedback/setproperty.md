# SetProperty

**Framework**: Force Feedback

This function sets properties that define the device behavior.

#### Overview

```c
HRESULT ( *SetProperty)(
   void *self,
   FFProperty property,
   void *pValue );
```

##### Parameters

##### Return Value

If the method succeeds, the return value is FF_OK or FFERR_UNSUPPORTED. If the method fails, the return value can be one of the following error values:

FFERR_INVALIDPARAM

## See Also

- [DestroyEffect](destroyeffect.md)
  This function commands the device to “destroy” a currently downloaded effect. The effect ID and any data that is associated with the effect are freed and available for reallocation.
- [DownloadEffect](downloadeffect.md)
  This function sends an effect to the device.
- [Escape](escape.md)
  This function escapes to the driver. This method is called in response to an application invoking the FFEffectEscape or FFDeviceEscape methods.
- [ForceFeedbackGetVersion](forcefeedbackgetversion.md)
  This function is used to determine driver and API version information.
- [GetEffectStatus](geteffectstatus.md)
  This function returns the device effect’s status.
- [GetForceFeedbackCapabilities](getforcefeedbackcapabilities.md)
  This function escapes to the driver. This method is called in response to an application invoking the FFEffectEscape or FFDevicEscape methods.
- [GetForceFeedbackState](getforcefeedbackstate.md)
  This function returns the state of the device.
- [InitializeTerminate](initializeterminate.md)
  This function is used to “create and destroy” particular device instances. It provides the FF plug-in driver with all the necessary start-up parameters.
- [SendForceFeedbackCommand](sendforcefeedbackcommand.md)
  This function sends a command to the device.
- [StartEffect](starteffect.md)
  This function commands the device to play back an effect that was previously loaded.
- [StopEffect](stopeffect.md)
  This function commands the device to stop an effect that was previously started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/setproperty)*