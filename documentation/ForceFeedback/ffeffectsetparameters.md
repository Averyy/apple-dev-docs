# FFEffectSetParameters(_:_:_:)

**Framework**: Force Feedback  
**Kind**: func

Sets the characteristics of an effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
func FFEffectSetParameters(_ effectReference: FFEffectObjectReference!, _ pFFEffect: UnsafeMutablePointer<FFEFFECT>!, _ flags: FFEffectParameterFlag) -> HRESULT
```

#### Return Value

If the method succeeds, the return value is FF_OK. If the method fails, the return value can be one of the following error values:

#### Discussion

FFERR_INVALIDPARAM

FFERR_UNSUPPORTEDAXIS

FFERR_OUTOFMEMORY

FFERR_DEVICEPAUSED

FFERR_DEVICEFULL

FFERR_INVALIDDOWNLOADID

FFERR_INTERNAL

FFERR_EFFECTTYPEMISMATCH

#### Discussion

The FFEffectSetParameters method automatically downloads the effect, but this behavior can be suppressed by setting the FFEP_NODOWNLOAD flag. If automatic download has been suppressed, you can manually download the effect by invoking the FFEffectDownload method.

If the effect is playing while the parameters are changed, the new parameters take effect as if they were the parameters when the effect started.

For example, suppose a periodic effect with a duration of three seconds is started. After two seconds, the direction of the effect is changed. The effect then continues for one additional second in the new direction. The envelope, phase, amplitude, and other parameters of the effect continue smoothly, as if the direction had not changed.

In the same situation, if after two seconds the duration of the effect were changed to 1.5 seconds, the effect would stop.

Normally, if the driver cannot update the parameters of a playing effect, the driver is permitted to stop the effect, update the parameters, and then restart the effect. Passing the FFEP_NORESTART flag suppresses this behavior. If the driver cannot update the parameters of an effect while it is playing, the error code FFERR_EFFECTPLAYING is returned, and the parameters are not updated.

No more than one of the FFEP_NODOWNLOAD, FFEP_START, and FFEP_NORESTART flags should be set. (It is also valid to pass none of them.)

These three flags control download and playback behavior as follows:

If FFEP_NODOWNLOAD is set, the effect parameters are updated but not downloaded to the device.

If the FFEP_START flag is set, the effect parameters are updated and downloaded to the device, and the effect is started just as if the FFEffect_Start method had been called with the dwIterations parameter set to 1 and with no flags. (Combining the update with FFEP_START is slightly faster than calling Start separately, because it requires less information to be transmitted to the device.)

If neither FFEP_NODOWNLOAD nor FFEP_START is set and the effect is not playing, the parameters are updated and downloaded to the device.

If neither FFEP_NODOWNLOAD nor FFEP_START is set and the effect is playing, the parameters are updated if the device supports on-the-fly updating. Otherwise the behavior depends on the state of the FFEP_NORESTART flag. If it is set, the error code FFERR_EFFECTPLAYING is returned. If it is clear, the effect is stopped, the parameters are updated, and the effect is restarted.

## Parameters

- `effectReference`: An opaque reference handle to an effect object. This is obtained from a previous call to FFDeviceCreateEffect.
- `pFFEffect`: Address of a FFEFFECT structure that contains effect information. The dwSize member must be filled in by the application before calling this method, as well as any members specified by corresponding bits in the flags parameter.
- `flags`: The lpvTypeSpecificParams and cbTypeSpecificParams members of the FFEFFECT structure contain the address and size of type-specific data for the effect.

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
- [func FFEffectDownload(FFEffectObjectReference!) -> HRESULT](ffeffectdownload(_:).md)
  Places the effect on the device. If the effect is already on the device, the existing effect is updated to match the values set by the FFEffectSetParameters method.
- [func FFEffectEscape(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFESCAPE>!) -> HRESULT](ffeffectescape(_:_:).md)
  Sends a hardware-specific command to the driver.
- [func FFEffectGetEffectStatus(FFEffectObjectReference!, UnsafeMutablePointer<FFEffectStatusFlag>!) -> HRESULT](ffeffectgeteffectstatus(_:_:).md)
  Sends a hardware-specific command to the driver.
- [func FFEffectGetParameters(FFEffectObjectReference!, UnsafeMutablePointer<FFEFFECT>!, FFEffectParameterFlag) -> HRESULT](ffeffectgetparameters(_:_:_:).md)
  Retrieves information about an effect.
- [func FFEffectStart(FFEffectObjectReference!, UInt32, FFEffectStartFlag) -> HRESULT](ffeffectstart(_:_:_:).md)
  Begins playing an effect. If the effect is already playing, it is restarted from the beginning. If the effect has not been downloaded or has been modified since its last download, it is downloaded before being started. This default behavior can be suppressed by passing the FFES_NODOWNLOAD flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffectsetparameters(_:_:_:))*