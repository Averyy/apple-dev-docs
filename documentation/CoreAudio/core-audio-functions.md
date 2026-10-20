# Core Audio Functions

**Framework**: Core Audio  
**Role**: API Collection

## Topics

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
- [func AudioHardwareDestroyAggregateDevice(AudioObjectID) -> OSStatus](./audiohardwaredestroyaggregatedevice%28_%29.md)
- [func AudioHardwareUnload() -> OSStatus](./audiohardwareunload%28%29.md)
- [func AudioObjectAddPropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audioobjectaddpropertylistener%28_,_,_,_%29.md)
- [func AudioObjectAddPropertyListenerBlock(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, dispatch_queue_t?, AudioObjectPropertyListenerBlock) -> OSStatus](./audioobjectaddpropertylistenerblock%28_,_,_,_%29.md)
- [func AudioObjectGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audioobjectgetpropertydata%28_,_,_,_,_,_%29.md)
- [func AudioObjectGetPropertyDataSize(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](./audioobjectgetpropertydatasize%28_,_,_,_,_%29.md)
- [func AudioObjectHasProperty(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>) -> Bool](./audioobjecthasproperty%28_,_%29.md)
- [func AudioObjectIsPropertySettable(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./audioobjectispropertysettable%28_,_,_%29.md)
- [func AudioObjectRemovePropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audioobjectremovepropertylistener%28_,_,_,_%29.md)
- [func AudioObjectRemovePropertyListenerBlock(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, dispatch_queue_t?, AudioObjectPropertyListenerBlock) -> OSStatus](./audioobjectremovepropertylistenerblock%28_,_,_,_%29.md)
- [func AudioObjectSetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](./audioobjectsetpropertydata%28_,_,_,_,_,_%29.md)
- [func AudioObjectShow(AudioObjectID)](./audioobjectshow%28_%29.md)
- [func AudioHardwareCreateProcessTap(CATapDescription!, UnsafeMutablePointer<AudioObjectID>!) -> OSStatus](./audiohardwarecreateprocesstap%28_,_%29.md)
- [func AudioHardwareDestroyProcessTap(AudioObjectID) -> OSStatus](./audiohardwaredestroyprocesstap%28_%29.md)
- [func PropertyAddress(AudioObjectPropertySelector, scope: AudioObjectPropertyScope, element: AudioObjectPropertyElement) -> AudioObjectPropertyAddress](./propertyaddress%28_,scope,element%29.md)
  A helper constructor for the AudioObjectPropertyAddress struct.

## See Also

### Reference
- [Core Audio Structures](./core-audio-structures.md)
- [Core Audio Data Types](./core-audio-data-types.md)
- [Core Audio Constants](./core-audio-constants.md)
- [Core Audio Enumerations](./core-audio-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/core-audio-functions)*