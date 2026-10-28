# FFDeviceGetForceFeedbackProperty(_:_:_:_:)

**Framework**: Force Feedback  
**Kind**: func  
**Role**: Function

Gets properties that define the device behavior.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
func FFDeviceGetForceFeedbackProperty(_ deviceReference: FFDeviceObjectReference!, _ property: FFProperty, _ pValue: UnsafeMutableRawPointer!, _ valueSize: IOByteCount) -> HRESULT
```

```c
extern HRESULT FFDeviceGetForceFeedbackProperty(FFDeviceObjectReference deviceReference, FFProperty property, void *pValue, IOByteCount valueSize);
```

## Return Value

If the method succeeds, the return value is FF_OK or FFERR_UNSUPPORTED. If the method fails, the return value can be one of the following error values:

## Discussion

FFERR_INVALIDPARAM

## Parameters

- `deviceReference`: An opaque reference handle to the device object that is be disposed of. This handle is obtained from a previous call to FFCreateDevice.
- `property`: The following property values are defined for a FF device (see FFDeviceSetForceFeedbackProperty for details):

  FFPROP_AUTOCENTER

  FFPROP_FFGAIN
- `pValue`: Address of the location where the value associated with the property is to be stored. GetForceFeedbackProperty assumes that the pointer is valid, although it will perform a size check before writing the data to pValue
- `valueSize`: Size, in bytes, of data area pointed to by pValue. Size is compared to expected property size, and the function fails if a mismatch occurs.

## See Also

### Miscellaneous
- [func FFCreateDevice(io_service_t, UnsafeMutablePointer<FFDeviceObjectReference?>!) -> HRESULT](./ffcreatedevice%28_,_%29.md)
  Creates a new API device object from an OS object in preparation to use the device for force feedback.
- [func FFDeviceCreateEffect(FFDeviceObjectReference!, CFUUID!, UnsafeMutablePointer<FFEFFECT>!, UnsafeMutablePointer<FFEffectObjectReference?>!) -> HRESULT](./ffdevicecreateeffect%28_,_,_,_%29.md)
  Creates and initializes an instance of an effect identified by the effect UUID on the device.
- [func FFDeviceEscape(FFDeviceObjectReference!, UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](./ffdeviceescape%28_,_%29.md)
  Sends a hardware-specific command to the device.
- [func FFDeviceGetForceFeedbackCapabilities(FFDeviceObjectReference!, UnsafeMutablePointer<FFCAPABILITIES>!) -> HRESULT](./ffdevicegetforcefeedbackcapabilities%28_,_%29.md)
  Retrieves the device’s force feedback capabilities.
- [func FFDeviceGetForceFeedbackState(FFDeviceObjectReference!, UnsafeMutablePointer<FFState>!) -> HRESULT](./ffdevicegetforcefeedbackstate%28_,_%29.md)
  Retrieves the state of the device’s force feedback system.
- [func FFDeviceReleaseEffect(FFDeviceObjectReference!, FFEffectObjectReference!) -> HRESULT](./ffdevicereleaseeffect%28_,_%29.md)
  Disposes of an API effect object created with FFDeviceCreateEffect.
- [func FFDeviceSendForceFeedbackCommand(FFDeviceObjectReference!, FFCommandFlag) -> HRESULT](./ffdevicesendforcefeedbackcommand%28_,_%29.md)
  Sends a command to the device’s force feedback system.
- [func FFDeviceSetCooperativeLevel(FFDeviceObjectReference!, UnsafeMutableRawPointer!, FFCooperativeLevelFlag) -> HRESULT](./ffdevicesetcooperativelevel%28_,_,_%29.md)
  Function is unimplemented in version 1.0 of this API
- [func FFDeviceSetForceFeedbackProperty(FFDeviceObjectReference!, FFProperty, UnsafeMutableRawPointer!) -> HRESULT](./ffdevicesetforcefeedbackproperty%28_,_,_%29.md)
  Retrieves the device’s force feedback capabilities.
- [func FFEffectDownload(FFEffectObjectReference!) -> HRESULT](./ffeffectdownload%28_%29.md)
  Places the effect on the device. If the effect is already on the device, the existing effect is updated to match the values set by the FFEffectSetParameters method.
- [func FFEffectEscape(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](./ffeffectescape%28_,_%29.md)
  Sends a hardware-specific command to the driver.
- [func FFEffectGetEffectStatus(FFEffectObjectReference!, UnsafeMutablePointer<FFEffectStatusFlag>!) -> HRESULT](./ffeffectgeteffectstatus%28_,_%29.md)
  Sends a hardware-specific command to the driver.
- [func FFEffectGetParameters(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFECT>!, FFEffectParameterFlag) -> HRESULT](./ffeffectgetparameters%28_,_,_%29.md)
  Retrieves information about an effect.
- [func FFEffectSetParameters(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFECT>!, FFEffectParameterFlag) -> HRESULT](./ffeffectsetparameters%28_,_,_%29.md)
  Sets the characteristics of an effect.
- [func FFEffectStart(FFEffectObjectReference!, UInt32, FFEffectStartFlag) -> HRESULT](./ffeffectstart%28_,_,_%29.md)
  Begins playing an effect. If the effect is already playing, it is restarted from the beginning. If the effect has not been downloaded or has been modified since its last download, it is downloaded before being started. This default behavior can be suppressed by passing the FFES_NODOWNLOAD flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffdevicegetforcefeedbackproperty(_:_:_:_:))*