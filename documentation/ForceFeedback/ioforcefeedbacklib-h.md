# IOForceFeedbackLib.h

**Framework**: Force Feedback

Public Interfaces and constants used to develop Force Feedback plugIns.

#### Overview

A force feedback device manufacturer might need to implement a plugIn to allow the Force Feedback Library to control the device. This header file describes the functions that need to be implemented. This interface definition follows Microsoft Windows IDirectInputEffectDriver definition wherever it makes sense to do so. This plugIn architecture uses the CFPlugIn model (COM). The Force Feedback Framework will find available plugIns and will use this interface to communicate with the hardware.

Certain functions may contain more or fewer parameters than the corresponding Windows IDirectInputEffectDriver version.

##### Included Headers

- <sys/cdefs.h>
- <CoreFoundation/CoreFoundation.h>
- <CoreFoundation/CFPlugInCOM.h>
- <MacTypes.h>
- <IOKit/IOTypes.h>
- <ForceFeedback/ForceFeedback.h>

## Topics

### Miscellaneous
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
- [SetProperty](setproperty.md)
  This function sets properties that define the device behavior.
- [StartEffect](starteffect.md)
  This function commands the device to play back an effect that was previously loaded.
- [StopEffect](stopeffect.md)
  This function commands the device to stop an effect that was previously started.
### Data Types
- [FFEffectDownloadID](ffeffectdownloadid.md)
  Unique identification for an effect.
- [ForceFeedbackDeviceState](forcefeedbackdevicestate.md)
  Returns information about the state of a force feedback device.
- [ForceFeedbackVersion](forcefeedbackversion.md)
  Used to return plugIn version information.
### Constants
- [Defines](defines.md)

## See Also

- [ForceFeedback.h](forcefeedback-h.md)
  Public Interfaces to the Force Feedback implementation in macOS.
- [ForceFeedbackConstants.h](forcefeedbackconstants-h.md)
  Constants used in the public interfaces to the Force Feedback implementation in macOS.
- [ForceFeedback Structures](forcefeedback-structures.md)
- [ForceFeedback Enumerations](forcefeedback-enumerations.md)
- [ForceFeedback Data Types](forcefeedback-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ioforcefeedbacklib-h)*