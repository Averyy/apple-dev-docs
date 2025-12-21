# AudioDeviceGetNearestStartTime(_:_:_:)

**Framework**: Core Audio  
**Kind**: func

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
func AudioDeviceGetNearestStartTime(_ inDevice: AudioObjectID, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus
```

#### Return Value

An OSStatus indicating success or failure. kAudioHardwareNotRunningError will be returned if the AudioDevice isn’t running. kAudioHardwareUnsupportedOperationError will be returned if the AudioDevice does not support starting at a specific time.

#### Discussion

Query an AudioDevice to get a time equal to or later than the given time that is the best time to start IO.

The time that is returned is dictated by the constraints of the device and the system. For instance, the driver of a device that provides both audio and video data may only allow start times that coincide with the edge of a video frame. Also, if the device already has one or more active IOProcs, the start time will be shifted to the beginning of the next IO cycle so as not to cause discontinuities in the existing IOProcs. Another reason the start time may shift is to allow for aligning the buffer accesses in an optimal fashion. Note that the device must be running to use this function.

## Parameters

- `inDevice`: The AudioDevice to query.
- `ioRequestedStartTime`: A pointer to an AudioTimeStamp that, on entry, is the requested start time.   On exit, it will have the a time equal to or later than the requested time,   as dictated by the device’s constraints.
- `inFlags`: A UInt32 containing flags that modify how this function behaves.

## See Also

- [func AudioConvertHostTimeToNanos(UInt64) -> UInt64](audioconverthosttimetonanos(_:).md)
- [func AudioConvertNanosToHostTime(UInt64) -> UInt64](audioconvertnanostohosttime(_:).md)
- [func AudioDeviceCreateIOProcID(AudioObjectID, AudioDeviceIOProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus](audiodevicecreateioprocid(_:_:_:_:).md)
- [func AudioDeviceCreateIOProcIDWithBlock(UnsafeMutablePointer<AudioDeviceIOProcID?>, AudioObjectID, dispatch_queue_t?, AudioDeviceIOBlock) -> OSStatus](audiodevicecreateioprocidwithblock(_:_:_:_:).md)
- [func AudioDeviceDestroyIOProcID(AudioObjectID, AudioDeviceIOProcID) -> OSStatus](audiodevicedestroyioprocid(_:_:).md)
- [func AudioDeviceGetCurrentTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audiodevicegetcurrenttime(_:_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodevicegetneareststarttime(_:_:_:))*