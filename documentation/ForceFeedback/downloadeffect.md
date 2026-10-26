# DownloadEffect

**Framework**: Force Feedback  
**Role**: Article

This function sends an effect to the device.

#### Overview

```c
HRESULT ( *DownloadEffect)(
   void *self,
   CFUUIDRef effectType,
   FFEffectDownloadID *pDownloadID,
   FFEFFECT *pEffect,
   FFEffectParameterFlag flags );
```

##### Parameters

- **self**: Pointer to the FFPlugInDriver implementation instance.
- **effectType**: Indicates the type of effect being created. Valid UUIDs are listed as kFFEffectType_* constants in the ForceFeedbackConstants.h file. (Supported effect types include Sine, Square, Triangle, SawtoothUp, SawtoothDown, Constant, Spring, Damper, etc.).
- **pDownloadID**: On entry, this parameter points to the handle of the effect being downloaded. If the parameter points to a zero, then a new effect is downloaded. On exit, the FFEffectDownloadID pointed to by this parameter contains the new effect handle. On failure, the FFEffectDownloadID pointed to by this parameter is set to zero if the effect is lost, or left alone if the effect is still valid with its old parameters. Note that zero is never a valid effect handle.
- **pEffect**: The new parameters for the effect.

  IMPORTANT NOTE: Unlike the IDirectInputEffectDriver specification, the axis and button values are NOT converted to object identifiers before they are handed over to the driver. In this case, the only supported method used to assign triggers and output axes is through object offsets, defined by the FFJOFS_* constants. Therefore, if a button is assigned to trigger an effect, FFEFFECT.dwTriggerButton will contain a constant of the form FFJOFS_BUTTONn. Similarly, output axes will be identified in FFEFFECT.rgdwAxes[n] as FFJOFS_X, FFJOFS_Y, etc.
- **flags**: Specifies which portions of the effect information have changed from the effect already on the device. This information is passed to drivers to allow for the optimization of effect modification. If an effect is being modified, a driver may be able to update the effect in its original position and transmit to the device only the information that has changed. Drivers are not, however, required to implement this optimization. All members of the FFEFFECT structure that are pointed to by the pEffect parameter are valid, and a driver may choose simply to update all parameters of the effect at each download. There may be zero, one, or more of the following:

  FFEP_DURATION

  Indicates the dwDuration member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download.

  FFEP_SAMPLEPERIOD

  Indicates the dwSamplePeriod member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download.

  FFEP_GAIN

  Indicates the dwGain member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download.

  FFEP_TRIGGERBUTTON

  Indicates the dwTriggerButton member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download.

  FFEP_TRIGGERREPEATINTERVAL

  Indicates the dwTriggerRepeatInterval member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download.

  FFEP_AXES

  Indicates the cAxes and rgdwAxes members of the FFEFFECT structure are being downloaded for the first time or have changed since their last download.

  FFEP_DIRECTION

  Indicates the cAxes and rglDirection members of the FFEFFECT structure are being downloaded for the first time or have changed since their last download. (The dwFlags member of the FFEFFECT structure specifies, through FFEFF_CARTESIAN or FFEFF_POLAR, the coordinate system in which the values should be interpreted.)

  FFEP_ENVELOPE

  Indicates the lpEnvelope member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download. If this flag is set and the lpEnvelope member is a NULL pointer, then the effect is being created with no envelope, or the existing envelope is being deleted.

  FFEP_TYPESPECIFICPARAMS

  Indicates the cbTypeSpecificParams and lpTypeSpecificParams members of the FFEFFECT structure are being downloaded for the first time or have changed since their last download.

  FFEP_STARTDELAY

  Indicates the dwStartDelay member of the FFEFFECT structure is being downloaded for the first time or has changed since its last download.

  FFEP_START

  Indicates that the effect is to be restarted from the beginning after the parameters of the effect have been updated. Note that the FFEP_NODOWNLOAD flag overrides the FFEP_START flag.

  FFEP_NORESTART

  If this flag is not specified, the effect device driver is permitted to restart the effect if doing so is necessary to change the specified parameters. Note that the FFEP_NODOWNLOAD and FFEP_START flags override this flag.

  FFEP_NODOWNLOAD

  Suppresses the automatic download that is normally performed after the parameters are updated. If this flag is set, the driver should validate parameters without performing an actual download.

##### Return Value

Returns FF_OK if successful, or an error value otherwise:

FFERR_DEVICEPAUSED

FFERR_DEVICEFULL

FFERR_INVALIDDOWNLOADID

FFERR_INTERNAL

FFERR_EFFECTTYPEMISMATCH

## See Also

### Miscellaneous
- [DestroyEffect](./destroyeffect.md)
  This function commands the device to “destroy” a currently downloaded effect. The effect ID and any data that is associated with the effect are freed and available for reallocation.
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
- [StartEffect](./starteffect.md)
  This function commands the device to play back an effect that was previously loaded.
- [StopEffect](./stopeffect.md)
  This function commands the device to stop an effect that was previously started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/downloadeffect)*