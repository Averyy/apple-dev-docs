# PropertyAddress(_:scope:element:)

**Framework**: Core Audio  
**Kind**: func

A helper constructor for the AudioObjectPropertyAddress struct.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func PropertyAddress(_ selector: AudioObjectPropertySelector, scope: AudioObjectPropertyScope = kAudioObjectPropertyScopeGlobal, element: AudioObjectPropertyElement = kAudioObjectPropertyElementMain) -> AudioObjectPropertyAddress
```

#### Return Value

An AudioObjectPropertyAddress collects these three parts that identify a specific property together in a struct for easy transmission.

## Parameters

- `selector`: An AudioObjectPropertySelector four char code that identifies a property
- `scope`: An AudioObjectPropertyScope with a default value of kAudioObjectPropertyScopeGlobal
- `element`: An AudioObjectPropertyElement with a default value of kAudioObjectPropertyElementMain

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/propertyaddress(_:scope:element:))*