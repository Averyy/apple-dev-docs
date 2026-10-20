# FFEffectStart(_:_:_:)

**Framework**: Force Feedback  
**Kind**: func  
**Role**: Function

Begins playing an effect. If the effect is already playing, it is restarted from the beginning. If the effect has not been downloaded or has been modified since its last download, it is downloaded before being started. This default behavior can be suppressed by passing the FFES_NODOWNLOAD flag.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
func FFEffectStart(_ effectReference: FFEffectObjectReference!, _ iterations: UInt32, _ flags: FFEffectStartFlag) -> HRESULT
```

```c
extern HRESULT FFEffectStart(FFEffectObjectReference effectReference, UInt32 iterations, FFEffectStartFlag flags);
```

#### Return Value

If the method succeeds, the return value is FF_OK. If the method fails, the return value can be one of the following error values:

#### Discussion

FFERR_INVALIDPARAM

FFERR_DEVICEPAUSED

FFERR_DEVICEFULL

FFERR_INVALIDDOWNLOADID

FFERR_INTERNAL

FFERR_EFFECTTYPEMISMATCH

FFERR_GENERIC

#### Discussion

Not all devices support multiple iterations.

## Parameters

- `effectReference`: An opaque reference handle to an effect object. This is obtained from a previous call to FFDeviceCreateEffect.
- `iterations`: Number of times to play the effect in sequence. The envelope is re-articulated with each iteration.

  To play the effect exactly once, pass 1. To play the effect repeatedly until explicitly stopped, pass INFINITE. To play the effect until explicitly stopped without re-articulating the envelope, modify the effect parameters with the FFEffect_SetParameters method, and change the dwDuration member to INFINITE.
- `flags`: Flags that describe how the effect should be played by the device. The value can be 0 or one or more of the following values:

  FFES_SOLO

  All other effects on the device should be stopped before the specified effect is played. If this flag is omitted, the effect is mixed with existing effects already started on the device.

  FFES_NODOWNLOAD

  Do not automatically download the effect.

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

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffectstart(_:_:_:))*