# AudioDeviceCreateIOProcID(_:_:_:_:)

**Framework**: Core Audio  
**Kind**: func

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafeMutableRawPointer?, _ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Creates an AudioDeviceIOProcID from an AudioDeviceIOProc and a client data pointer.

AudioDeviceIOProcIDs allow for the client to register the same function pointer with a device multiple times

## Parameters

- `inDevice`: The AudioDevice to register the IOProc with.
- `inProc`: The AudioDeviceIOProc to register.
- `inClientData`: A pointer to client data that is passed back to the IOProc when it is   called.
- `outIOProcID`: The newly created AudioDeviceIOProcID.

## See Also

- [func AudioConvertHostTimeToNanos(UInt64) -> UInt64](audioconverthosttimetonanos(_:).md)
- [func AudioConvertNanosToHostTime(UInt64) -> UInt64](audioconvertnanostohosttime(_:).md)
- [func AudioDeviceCreateIOProcIDWithBlock(UnsafeMutablePointer<AudioDeviceIOProcID?>, AudioObjectID, dispatch_queue_t?, AudioDeviceIOBlock) -> OSStatus](audiodevicecreateioprocidwithblock(_:_:_:_:).md)
- [func AudioDeviceDestroyIOProcID(AudioObjectID, AudioDeviceIOProcID) -> OSStatus](audiodevicedestroyioprocid(_:_:).md)
- [func AudioDeviceGetCurrentTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audiodevicegetcurrenttime(_:_:).md)
- [func AudioDeviceGetNearestStartTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audiodevicegetneareststarttime(_:_:_:).md)
- [func AudioDeviceStart(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](audiodevicestart(_:_:).md)
- [func AudioDeviceStartAtTime(AudioObjectID, AudioDeviceIOProcID?, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audiodevicestartattime(_:_:_:_:).md)
- [func AudioDeviceStop(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](audiodevicestop(_:_:).md)
- [func AudioDeviceTranslateTime(AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audiodevicetranslatetime(_:_:_:).md)
- [func AudioGetCurrentHostTime() -> UInt64](audiogetcurrenthosttime().md)
- [func AudioGetHostClockFrequency() -> Float64](audiogethostclockfrequency().md)
- [func AudioGetHostClockMinimumTimeDelta() -> UInt32](audiogethostclockminimumtimedelta().md)
- [func AudioHardwareCreateAggregateDevice(CFDictionary, UnsafeMutablePointer<AudioObjectID>) -> OSStatus](audiohardwarecreateaggregatedevice(_:_:).md)
- [func AudioHardwareDestroyAggregateDevice(AudioObjectID) -> OSStatus](audiohardwaredestroyaggregatedevice(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodevicecreateioprocid(_:_:_:_:))*