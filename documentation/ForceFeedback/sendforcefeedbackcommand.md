# SendForceFeedbackCommand

**Framework**: Force Feedback  
**Role**: Article

This function sends a command to the device.

#### Overview

```c
HRESULT ( *SendForceFeedbackCommand)(
   void *self,
   FFCommandFlag state );
```

##### Parameters

- **self**: Pointer to the FFPlugInDriver implementation instance.
- **state**: Indicates the command being sent. That command can be one of the following:

  FFSFFC_RESET

  Indicates that playback of any active effects should be been stopped and that all effects should be removed from the device. Once the device has been reset, all effects are no longer valid and must be re-created.

  FFSFFC_STOPALL

  Indicates that playback of all effects should be stopped. Sending the FFSFFC_STOPALL command is equivalent to invoking the FFEffect_Stop method on all effects that are playing. If the device is in a paused state, the device driver is permitted to lose the paused state.

  FFSFFC_PAUSE

  Indicates that playback of all effects should be paused. When effects are paused, time “stops” until the FFSFFC_CONTINUE command is sent. For example, suppose an effect of five seconds’ duration is started. After one second, all effects are paused. After two more seconds, all effects are continued. The effect should then play for four additional seconds. While a force-feedback device is paused, starting a new effect or modifying existing ones can cause the paused state to be lost.

  FFSFFC_CONTINUE

  Indicates that playback should be resumed at the point at which it was interrupted for those effects that were paused by a previous FFSCFFC_PAUSE command.

  FFSFFC_SETACTUATORSON

  Indicates that the device’s force-feedback actuators should be enabled.

  FFSFFC_SETACTUATORSOFF

  Indicates that the device’s force-feedback actuators should be disabled. If successful, force-feedback effects are “muted”. Note that time continues to elapse while actuators are off. For example, suppose an effect of five seconds’ duration is started. After one second, actuators are turned off. After two more seconds, actuators are turned back on. The effect should then play for two additional seconds.

##### Return Value

Returns FF_OK if successful, or an error value otherwise:

FFERR_INTERNAL

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
- [SetProperty](./setproperty.md)
  This function sets properties that define the device behavior.
- [StartEffect](./starteffect.md)
  This function commands the device to play back an effect that was previously loaded.
- [StopEffect](./stopeffect.md)
  This function commands the device to stop an effect that was previously started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/sendforcefeedbackcommand)*