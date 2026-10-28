# FFIsForceFeedback(_:)

**Framework**: Force Feedback  
**Kind**: func  
**Role**: Function

Used to determine if a particular device provided by HID Manager is a force feedback device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
func FFIsForceFeedback(_ hidDevice: io_service_t) -> HRESULT
```

```c
extern HRESULT FFIsForceFeedback(io_service_t hidDevice);
```

## Return Value

If the method succeeds, and the device supports FF, the return value is FF_OK. If the method succeeds, and the device does not support FF, the return value is FFERR_NOINTERFACE. If the method fails, the return value is FFERR_INVALIDPARAM

## Discussion

When you are finished with the device, FFReleaseDevice must be called on the reference received in this function to dispose of the API device object.

## Parameters

- `hidDevice`: Pointer to a HID device object to be tested for force feedback support.

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
- [func FFDeviceGetForceFeedbackProperty(FFDeviceObjectReference!, FFProperty, UnsafeMutableRawPointer!, IOByteCount) -> HRESULT](./ffdevicegetforcefeedbackproperty%28_,_,_,_%29.md)
  Gets properties that define the device behavior.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffisforcefeedback(_:))*