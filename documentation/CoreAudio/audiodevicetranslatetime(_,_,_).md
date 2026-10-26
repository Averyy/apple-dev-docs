# AudioDeviceTranslateTime(_:_:_:)

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func AudioDeviceTranslateTime(_ inDevice: AudioObjectID, _ inTime: UnsafePointer<AudioTimeStamp>, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus
```

```c
extern OSStatus AudioDeviceTranslateTime(AudioObjectID inDevice, const AudioTimeStamp *inTime, AudioTimeStamp *outTime);
```

#### Return Value

An OSStatus indicating success or failure. kAudioHardwareNotRunningError will be returned if the AudioDevice isn’t running.

#### Discussion

Translates the time in the AudioDevice’s time base from one representation to another. Note that the device has to be running

## Parameters

- `inDevice`: The AudioDevice whose time base governs the translation.
- `inTime`: An AudioTimeStamp containing the time to be translated.
- `outTime`: An AudioTimeStamp into which the translated time is put. On entry, the mFlags field specifies which representations to translate the input time into. Because not every device supports all time representations, on exit, the mFlags field will indicate which translations were actually done.

## See Also

### Functions
- [func AudioConvertHostTimeToNanos(UInt64) -> UInt64](./audioconverthosttimetonanos%28_%29.md)
- [func AudioConvertNanosToHostTime(UInt64) -> UInt64](./audioconvertnanostohosttime%28_%29.md)
- [func AudioDeviceCreateIOProcID(AudioObjectID, AudioDeviceIOProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus](./audiodevicecreateioprocid%28_,_,_,_%29.md)
- [func AudioDeviceCreateIOProcIDWithBlock(UnsafeMutablePointer<AudioDeviceIOProcID?>, AudioObjectID, dispatch_queue_t?, AudioDeviceIOBlock) -> OSStatus](./audiodevicecreateioprocidwithblock%28_,_,_,_%29.md)
- [func AudioDeviceDestroyIOProcID(AudioObjectID, AudioDeviceIOProcID) -> OSStatus](./audiodevicedestroyioprocid%28_,_%29.md)
- [func AudioDeviceGetCurrentTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audiodevicegetcurrenttime%28_,_%29.md)
- [func AudioDeviceGetNearestStartTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audiodevicegetneareststarttime%28_,_,_%29.md)
- [func AudioDeviceStart(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](./audiodevicestart%28_,_%29.md)
- [func AudioDeviceStartAtTime(AudioObjectID, AudioDeviceIOProcID?, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audiodevicestartattime%28_,_,_,_%29.md)
- [func AudioDeviceStop(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](./audiodevicestop%28_,_%29.md)
- [func AudioGetCurrentHostTime() -> UInt64](./audiogetcurrenthosttime%28%29.md)
- [func AudioGetHostClockFrequency() -> Float64](./audiogethostclockfrequency%28%29.md)
- [func AudioGetHostClockMinimumTimeDelta() -> UInt32](./audiogethostclockminimumtimedelta%28%29.md)
- [func AudioHardwareCreateAggregateDevice(CFDictionary, UnsafeMutablePointer<AudioObjectID>) -> OSStatus](./audiohardwarecreateaggregatedevice%28_,_%29.md)
- [func AudioHardwareDestroyAggregateDevice(AudioObjectID) -> OSStatus](./audiohardwaredestroyaggregatedevice%28_%29.md)
- [AudioDriverPlugInClose](./audiodriverpluginclose.md)
- [AudioDriverPlugInDeviceGetProperty](./audiodriverplugindevicegetproperty.md)
- [AudioDriverPlugInDeviceGetPropertyInfo](./audiodriverplugindevicegetpropertyinfo.md)
- [AudioDriverPlugInDeviceSetProperty](./audiodriverplugindevicesetproperty.md)
- [AudioDriverPlugInOpen](./audiodriverpluginopen.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodevicetranslatetime(_:_:_:))*