# AudioHardwareServiceGetPropertyDataSize(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the payload size for a given property.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func AudioHardwareServiceGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>!, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafeRawPointer!, _ outDataSize: UnsafeMutablePointer<UInt32>!) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inObjectID`: The HAL audio object to query.
- `inAddress`: The property whose payload size you want.
- `inQualifierDataSize`: A   value indicating the size of the buffer pointed to by the   parameter. Not all properties require qualification; in such a case you set this parameter to  .
- `inQualifierData`: A buffer of data to be used in determining the value of the property being queried. Not all properties require qualification; in such a case you set this parameter to  .
- `outDataSize`: A   value indicating the size, in bytes, of the payload for the given property.

## See Also

- [func AudioHardwareServiceGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](audiohardwareservicegetpropertydata(_:_:_:_:_:_:).md)
  Gets the value for a specified property.
- [func AudioFileReadPackets(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audiofilereadpackets(_:_:_:_:_:_:_:).md)
  Reads a fixed duration of audio data from an audio file.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](audiocomponentgeticon(_:).md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](audiocomponentgetlastactivetime(_:).md)
  The time at which the application publishing the component was last active.
- [func AudioHardwareServiceAddPropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, AudioObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](audiohardwareserviceaddpropertylistener(_:_:_:_:).md)
  Registers a HAL audio object property listener callback function to be invoked when a specified property changes.
- [func AudioHardwareServiceGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](audiohardwareservicegetpropertydata(_:_:_:_:_:_:).md)
  Gets the value for a specified property.
- [func AudioHardwareServiceHasProperty(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!) -> Bool](audiohardwareservicehasproperty(_:_:).md)
  Queries a HAL audio object about whether or not it has a specified property.
- [func AudioHardwareServiceIsPropertySettable(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](audiohardwareserviceispropertysettable(_:_:_:).md)
  Queries a HAL audio object about whether a specified property is settable.
- [func AudioHardwareServiceRemovePropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, AudioObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](audiohardwareserviceremovepropertylistener(_:_:_:_:).md)
  Unregisters a HAL audio object property listener callback function.
- [func AudioHardwareServiceSetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UInt32, UnsafeRawPointer!) -> OSStatus](audiohardwareservicesetpropertydata(_:_:_:_:_:_:).md)
  Asks a HAL audio object to change the value of a specified property.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](audiooutputunitgethosticon(_:_:).md)
  The host app’s icon.
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](audiooutputunitpublish(_:_:_:_:).md)
  Registers an audio output unit for use by other applications.
- [func AudioSessionAddPropertyListener(AudioSessionPropertyID, AudioSessionPropertyListener!, UnsafeMutableRawPointer!) -> OSStatus](audiosessionaddpropertylistener(_:_:_:).md)
  Adds a property listener callback function to your application’s audio session object.
- [func AudioSessionGetProperty(AudioSessionPropertyID, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](audiosessiongetproperty(_:_:_:).md)
  Gets the value of a specified audio session property.
- [func AudioSessionGetPropertySize(AudioSessionPropertyID, UnsafeMutablePointer<UInt32>!) -> OSStatus](audiosessiongetpropertysize(_:_:).md)
  Gets the size of the value for a specified audio session property.
- [func AudioSessionInitialize(CFRunLoop!, CFString!, AudioSessionInterruptionListener!, UnsafeMutableRawPointer!) -> OSStatus](audiosessioninitialize(_:_:_:_:).md)
  Initializes an iOS application’s audio session object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiohardwareservicegetpropertydatasize(_:_:_:_:_:))*