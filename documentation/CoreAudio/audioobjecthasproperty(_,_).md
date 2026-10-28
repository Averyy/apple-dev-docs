# AudioObjectHasProperty(_:_:)

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func AudioObjectHasProperty(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>) -> Bool
```

```c
extern Boolean AudioObjectHasProperty(AudioObjectID inObjectID, const AudioObjectPropertyAddress *inAddress);
```

## Return Value

A Boolean indicating whether or not the AudioObject has the given property.

## Discussion

Queries an AudioObject about whether or not it has the given property.

## Parameters

- `inObjectID`: The AudioObject to query.
- `inAddress`: An AudioObjectPropertyAddress indicating which property is being queried.

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
- [func AudioDeviceTranslateTime(AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audiodevicetranslatetime%28_,_,_%29.md)
- [func AudioGetCurrentHostTime() -> UInt64](./audiogetcurrenthosttime%28%29.md)
- [func AudioGetHostClockFrequency() -> Float64](./audiogethostclockfrequency%28%29.md)
- [func AudioGetHostClockMinimumTimeDelta() -> UInt32](./audiogethostclockminimumtimedelta%28%29.md)
- [func AudioHardwareCreateAggregateDevice(CFDictionary, UnsafeMutablePointer<AudioObjectID>) -> OSStatus](./audiohardwarecreateaggregatedevice%28_,_%29.md)
- [AudioDriverPlugInClose](./audiodriverpluginclose.md)
- [AudioDriverPlugInDeviceGetProperty](./audiodriverplugindevicegetproperty.md)
- [AudioDriverPlugInDeviceGetPropertyInfo](./audiodriverplugindevicegetpropertyinfo.md)
- [AudioDriverPlugInDeviceSetProperty](./audiodriverplugindevicesetproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjecthasproperty(_:_:))*