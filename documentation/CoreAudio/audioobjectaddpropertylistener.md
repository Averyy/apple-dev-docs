# AudioObjectAddPropertyListener(_:_:_:_:)

**Framework**: Core Audio  
**Kind**: func

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Registers the given AudioObjectPropertyListenerProc to receive notifications when the given properties change.

## Parameters

- `inObjectID`: The AudioObject to register the listener with.
- `inAddress`: The AudioObjectPropertyAddresses indicating which property the listener   should be notified about.
- `inListener`: The AudioObjectPropertyListenerProc to call.
- `inClientData`: A pointer to client data that is passed to the listener when it is called.

## See Also

- [func AudioConvertHostTimeToNanos(UInt64) -> UInt64](audioconverthosttimetonanos(_:).md)
- [func AudioConvertNanosToHostTime(UInt64) -> UInt64](audioconvertnanostohosttime(_:).md)
- [func AudioDeviceCreateIOProcID(AudioObjectID, AudioDeviceIOProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus](audiodevicecreateioprocid(_:_:_:_:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectaddpropertylistener(_:_:_:_:))*