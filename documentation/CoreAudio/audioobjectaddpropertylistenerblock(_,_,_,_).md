# AudioObjectAddPropertyListenerBlock(_:_:_:_:)

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t?, _ inListener: @escaping AudioObjectPropertyListenerBlock) -> OSStatus
```

```c
extern OSStatus AudioObjectAddPropertyListenerBlock(AudioObjectID inObjectID, const AudioObjectPropertyAddress *inAddress, dispatch_queue_t inDispatchQueue, AudioObjectPropertyListenerBlock inListener);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Registers the given AudioObjectPropertyListenerBlock to receive notifications when the given properties change.

## Parameters

- `inObjectID`: The AudioObject to register the listener with.
- `inAddress`: The AudioObjectPropertyAddresses indicating which property the listener should be notified about.
- `inDispatchQueue`: The dispatch queue on which the listener block will be dispatched. All listener blocks will be dispatched asynchronously save for those dispatched from the IO context (of which kAudioDevicePropertyDeviceIsRunning and kAudioDeviceProcessorOverload are the only examples) which will be dispatched synchronously. Note that this dispatch queue will be retained until a matching call to AudioObjectRemovePropertyListenerBlock is made. If this value is NULL, then the block will be directly invoked.
- `inListener`: The AudioObjectPropertyListenerBlock to call. Note that this block will be Block_copy’d and the reference maintained until a matching call to AudioObjectRemovePropertyListenerBlock is made.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectaddpropertylistenerblock(_:_:_:_:))*