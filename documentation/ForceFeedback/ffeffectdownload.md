# FFEffectDownload(_:)

**Framework**: Force Feedback  
**Kind**: func

Places the effect on the device. If the effect is already on the device, the existing effect is updated to match the values set by the FFEffectSetParameters method.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
func FFEffectDownload(_ effectReference: FFEffectObjectReference!) -> HRESULT
```

#### Return Value

If the method succeeds, the return value is FF_OK or S_FALSE. If the method fails, the return value can be one of the following error values:

#### Discussion

FFERR_INVALIDPARAM

FFERR_DEVICEPAUSED

FFERR_DEVICEFULL

FFERR_INVALIDDOWNLOADID

FFERR_INTERNAL

FFERR_EFFECTTYPEMISMATCH

If the method returns S_FALSE, the effect has already been downloaded to the device.

#### Discussion

It is valid to update an effect while it is playing. The semantics of such an operation are explained in the reference for FFEffectSetParameters.

## Parameters

- `effectReference`: An opaque reference handle to an effect object. This is obtained from a previous call to FFDeviceCreateEffect.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffectdownload(_:))*