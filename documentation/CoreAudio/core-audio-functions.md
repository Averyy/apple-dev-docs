# Core Audio Functions

**Framework**: Core Audio

## Topics

### Functions
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
- [func AudioHardwareDestroyAggregateDevice(AudioObjectID) -> OSStatus](audiohardwaredestroyaggregatedevice(_:).md)
- [func AudioHardwareUnload() -> OSStatus](audiohardwareunload().md)
- [func AudioObjectAddPropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioobjectaddpropertylistener(_:_:_:_:).md)
- [func AudioObjectAddPropertyListenerBlock(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, dispatch_queue_t?, AudioObjectPropertyListenerBlock) -> OSStatus](audioobjectaddpropertylistenerblock(_:_:_:_:).md)
- [func AudioObjectGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioobjectgetpropertydata(_:_:_:_:_:_:).md)
- [func AudioObjectGetPropertyDataSize(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audioobjectgetpropertydatasize(_:_:_:_:_:).md)
- [func AudioObjectHasProperty(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>) -> Bool](audioobjecthasproperty(_:_:).md)
- [func AudioObjectIsPropertySettable(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](audioobjectispropertysettable(_:_:_:).md)
- [func AudioObjectRemovePropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioobjectremovepropertylistener(_:_:_:_:).md)
- [func AudioObjectRemovePropertyListenerBlock(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, dispatch_queue_t?, AudioObjectPropertyListenerBlock) -> OSStatus](audioobjectremovepropertylistenerblock(_:_:_:_:).md)
- [func AudioObjectSetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](audioobjectsetpropertydata(_:_:_:_:_:_:).md)
- [func AudioObjectShow(AudioObjectID)](audioobjectshow(_:).md)
- [func AudioHardwareCreateProcessTap(CATapDescription!, UnsafeMutablePointer<AudioObjectID>!) -> OSStatus](audiohardwarecreateprocesstap(_:_:).md)
- [func AudioHardwareDestroyProcessTap(AudioObjectID) -> OSStatus](audiohardwaredestroyprocesstap(_:).md)
- [func PropertyAddress(AudioObjectPropertySelector, scope: AudioObjectPropertyScope, element: AudioObjectPropertyElement) -> AudioObjectPropertyAddress](propertyaddress(_:scope:element:).md)

## See Also

- [Core Audio Structures](core-audio-structures.md)
- [Core Audio Data Types](core-audio-data-types.md)
- [Core Audio Constants](core-audio-constants.md)
- [Core Audio Enumerations](core-audio-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/core-audio-functions)*