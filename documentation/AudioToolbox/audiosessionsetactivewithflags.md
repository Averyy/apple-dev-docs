# AudioSessionSetActiveWithFlags(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Activates or deactivates your application’s audio session; provides flags for use by other audio sessions.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func AudioSessionSetActiveWithFlags(_ active: Bool, _ inFlags: UInt32) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Activating your audio session may interrupt audio sessions belonging to other applications running in the background, depending on categories and priorities. Deactivating your audio session allows other, interrupted audio sessions to resume.

When another active audio session does not allow mixing, attempting to activate your audio session may fail.

## Parameters

- `active`: Pass   to activate your application’s audio session, or   to deactivate it.
- `inFlags`: A bitmapped value containing one or more flags from the   enumeration.

## See Also

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
- [func AudioHardwareServiceGetPropertyDataSize(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!) -> OSStatus](audiohardwareservicegetpropertydatasize(_:_:_:_:_:).md)
  Gets the payload size for a given property.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiosessionsetactivewithflags(_:_:))*