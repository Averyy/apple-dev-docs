# AudioDeviceCreateIOProcID(_:_:_:_:)

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafeMutableRawPointer?, _ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus
```

```c
extern OSStatus AudioDeviceCreateIOProcID(AudioObjectID inDevice, AudioDeviceIOProc inProc, void *inClientData, AudioDeviceIOProcID*outIOProcID);
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

Creates an AudioDeviceIOProcID from an AudioDeviceIOProc and a client data pointer.

AudioDeviceIOProcIDs allow for the client to register the same function pointer with a device multiple times

## Parameters

- `inDevice`: The AudioDevice to register the IOProc with.
- `inProc`: The AudioDeviceIOProc to register.
- `inClientData`: A pointer to client data that is passed back to the IOProc when it is called.
- `outIOProcID`: The newly created AudioDeviceIOProcID.

## See Also

### Functions
- [func AudioConvertHostTimeToNanos(UInt64) -> UInt64](./audioconverthosttimetonanos%28_%29.md)
- [func AudioConvertNanosToHostTime(UInt64) -> UInt64](./audioconvertnanostohosttime%28_%29.md)
- [func AudioDeviceCreateIOProcIDWithBlock(UnsafeMutablePointer<AudioDeviceIOProcID?>, AudioObjectID, dispatch_queue_t?, AudioDeviceIOBlock) -> OSStatus](./audiodevicecreateioprocidwithblock%28_,_,_,_%29.md)
- [func AudioDeviceDestroyIOProcID(AudioObjectID, AudioDeviceIOProcID) -> OSStatus](./audiodevicedestroyioprocid%28_,_%29.md)
- [func AudioDeviceGetCurrentTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audiodevicegetcurrenttime%28_,_%29.md)
- [func AudioDeviceGetNearestStartTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audiodevicegetneareststarttime%28_,_,_%29.md)
- [func AudioDeviceStart(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](./audiodevicestart%28_,_%29.md)
- [func AudioDeviceStartAtTime(AudioObjectID, AudioDeviceIOProcID?, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audiodevicestartattime%28_,_,_,_%29.md)
- [func AudioDeviceStop(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](./audiodevicestop%28_,_%29.md)
- [func AudioDeviceTranslateTime(AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audiodevicetranslatetime%28_,_,_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodevicecreateioprocid(_:_:_:_:))*