# ForceFeedback.h

**Framework**: Force Feedback

Public Interfaces to the Force Feedback implementation in macOS.

#### Overview

The Force Feedback API allows developers to control Force Feedback devices attached to the system. It is a distilled version of the Force Feedback functionality found in Microsoft’s DirectInput API. Developers familiar with that API should find this API to be similar.

##### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <CoreFoundation/CFPlugInCOM.h>
- <MacTypes.h>
- <IOKit/IOTypes.h>
- <ForceFeedback/ForceFeedbackConstants.h>

## Topics

### Miscellaneous
- [func FFCreateDevice(io_service_t, UnsafeMutablePointer<FFDeviceObjectReference?>!) -> HRESULT](ffcreatedevice(_:_:).md)
  Creates a new API device object from an OS object in preparation to use the device for force feedback.
- [func FFDeviceCreateEffect(FFDeviceObjectReference!, CFUUID!, UnsafeMutablePointer<FFEFFECT>!, UnsafeMutablePointer<FFEffectObjectReference?>!) -> HRESULT](ffdevicecreateeffect(_:_:_:_:).md)
  Creates and initializes an instance of an effect identified by the effect UUID on the device.
- [func FFDeviceEscape(FFDeviceObjectReference!, UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](ffdeviceescape(_:_:).md)
  Sends a hardware-specific command to the device.
- [func FFDeviceGetForceFeedbackCapabilities(FFDeviceObjectReference!, UnsafeMutablePointer<FFCAPABILITIES>!) -> HRESULT](ffdevicegetforcefeedbackcapabilities(_:_:).md)
  Retrieves the device’s force feedback capabilities.
- [func FFDeviceGetForceFeedbackProperty(FFDeviceObjectReference!, FFProperty, UnsafeMutableRawPointer!, IOByteCount) -> HRESULT](ffdevicegetforcefeedbackproperty(_:_:_:_:).md)
  Gets properties that define the device behavior.
- [func FFDeviceGetForceFeedbackState(FFDeviceObjectReference!, UnsafeMutablePointer<FFState>!) -> HRESULT](ffdevicegetforcefeedbackstate(_:_:).md)
  Retrieves the state of the device’s force feedback system.
- [func FFDeviceReleaseEffect(FFDeviceObjectReference!, FFEffectObjectReference!) -> HRESULT](ffdevicereleaseeffect(_:_:).md)
  Disposes of an API effect object created with FFDeviceCreateEffect.
- [func FFDeviceSendForceFeedbackCommand(FFDeviceObjectReference!, FFCommandFlag) -> HRESULT](ffdevicesendforcefeedbackcommand(_:_:).md)
  Sends a command to the device’s force feedback system.
- [func FFDeviceSetCooperativeLevel(FFDeviceObjectReference!, UnsafeMutableRawPointer!, FFCooperativeLevelFlag) -> HRESULT](ffdevicesetcooperativelevel(_:_:_:).md)
  Function is unimplemented in version 1.0 of this API
- [func FFDeviceSetForceFeedbackProperty(FFDeviceObjectReference!, FFProperty, UnsafeMutableRawPointer!) -> HRESULT](ffdevicesetforcefeedbackproperty(_:_:_:).md)
  Retrieves the device’s force feedback capabilities.
- [func FFEffectDownload(FFEffectObjectReference!) -> HRESULT](ffeffectdownload(_:).md)
  Places the effect on the device. If the effect is already on the device, the existing effect is updated to match the values set by the FFEffectSetParameters method.
- [func FFEffectEscape(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](ffeffectescape(_:_:).md)
  Sends a hardware-specific command to the driver.
- [func FFEffectGetEffectStatus(FFEffectObjectReference!, UnsafeMutablePointer<FFEffectStatusFlag>!) -> HRESULT](ffeffectgeteffectstatus(_:_:).md)
  Sends a hardware-specific command to the driver.
- [func FFEffectGetParameters(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFECT>!, FFEffectParameterFlag) -> HRESULT](ffeffectgetparameters(_:_:_:).md)
  Retrieves information about an effect.
- [func FFEffectSetParameters(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFECT>!, FFEffectParameterFlag) -> HRESULT](ffeffectsetparameters(_:_:_:).md)
  Sets the characteristics of an effect.
- [func FFEffectStart(FFEffectObjectReference!, UInt32, FFEffectStartFlag) -> HRESULT](ffeffectstart(_:_:_:).md)
  Begins playing an effect. If the effect is already playing, it is restarted from the beginning. If the effect has not been downloaded or has been modified since its last download, it is downloaded before being started. This default behavior can be suppressed by passing the FFES_NODOWNLOAD flag.
- [func FFEffectStop(FFEffectObjectReference!) -> HRESULT](ffeffectstop(_:).md)
  Stops playing an effect.
- [func FFEffectUnload(FFEffectObjectReference!) -> HRESULT](ffeffectunload(_:).md)
  Removes the effect from the device. If the effect is playing, it is automatically stopped before it is unloaded.
- [func FFIsForceFeedback(io_service_t) -> HRESULT](ffisforcefeedback(_:).md)
  Used to determine if a particular device provided by HID Manager is a force feedback device.
- [func FFReleaseDevice(FFDeviceObjectReference!) -> HRESULT](ffreleasedevice(_:).md)
  Disposes of an API device object created with FFCreateDevice.
### Data Types
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
- [struct FFEFFESCAPE](ffeffescape.md)
  The FFEFFESCAPE structure passes hardware-specific data directly to the Force Feedback plugIn.
- [struct FFENVELOPE](ffenvelope.md)
  Used by the FFEFFECT structure to specify the optional envelope parameters for an effect.
- [struct FFPERIODIC](ffperiodic.md)
  A structure containing type-specific information for certain effects.
- [struct FFRAMPFORCE](fframpforce.md)
  Contains type-specific information for the RAMPFORCE effect.

## See Also

- [ForceFeedbackConstants.h](forcefeedbackconstants-h.md)
  Constants used in the public interfaces to the Force Feedback implementation in macOS.
- [ForceFeedback Enumerations](forcefeedback-enumerations.md)
- [ForceFeedback Constants](forcefeedback-constants.md)
- [ForceFeedback Data Types](forcefeedback-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/forcefeedback-h)*