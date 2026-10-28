# InitializeTerminate

**Framework**: Force Feedback  
**Role**: Article

This function is used to “create and destroy” particular device instances. It provides the FF plug-in driver with all the necessary start-up parameters.

## Overview

```c
HRESULT ( *InitializeTerminate)(
   void *self,
   NumVersion forceFeedbackAPIVersion,
   io_object_t hidDevice,
   boolean_t begin );
```

### Parameters

- **self**: Pointer to the FFPlugInDriver implementation instance.
- **forceFeedbackAPIVersion**: The version number of FF API that loaded the effect driver. The plugIn should check that the major version of the forceFeedbackAPI version is the same as the major version of the API at the time the plugIn was compiled. If the major versions are different, then the plugIn API has changed and the plugIn will NOT be compatible with it.

  If begin is false, this parameter is ignored.
- **hidDevice**: A device object that can be used by the FF plug-in to establish a connection to and communicate with the device. The caller will release the hidDevice device object with a call to IOObjectRelease() once the FF plug-in completes its InitializeTerminate processing, so a FF plug-in implementation should not make a copy of the io_object_t variable with the intention of using it outside the context of this call.

  If begin is false, this parameter is ignored. (You can pass NULL.)
- **begin**: Nonzero if access to the device is beginning. Zero if the access to the device is ending. The FF API will call InitializeTerminate( begin=TRUE) when a FF device is first selected for use, and InitializeTerminate( begin=false) when the FF device is no longer needed.

### Return Value

Returns FF_OK if successful, or an error value otherwise:

FFERR_INVALIDPARAM

FFERR_NOINTERFACE

FFERR_OUTOFMEMORY

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
- [SendForceFeedbackCommand](./sendforcefeedbackcommand.md)
  This function sends a command to the device.
- [SetProperty](./setproperty.md)
  This function sets properties that define the device behavior.
- [StartEffect](./starteffect.md)
  This function commands the device to play back an effect that was previously loaded.
- [StopEffect](./stopeffect.md)
  This function commands the device to stop an effect that was previously started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/initializeterminate)*