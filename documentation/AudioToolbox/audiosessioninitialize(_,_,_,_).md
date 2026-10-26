# AudioSessionInitialize(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Initializes an iOS application’s audio session object.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
func AudioSessionInitialize(_ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inInterruptionListener: AudioSessionInterruptionListener!, _ inClientData: UnsafeMutableRawPointer!) -> OSStatus
```

```c
extern OSStatus AudioSessionInitialize(CFRunLoopRef inRunLoop, CFStringRef inRunLoopMode, AudioSessionInterruptionListener inInterruptionListener, void *inClientData);
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Your application must call this function before making any other Audio Session Services calls. You may activate and deactivate your audio session as needed (see [`AudioSessionSetActive(_:)`](./audiosessionsetactive%28_%29.md)), but should initialize it only once.

## Parameters

- `inRunLoop`: The run loop  that the interruption listener callback should be run on. Pass `NULL` to use the main run loop.
- `inRunLoopMode`: The mode for the run loop that the interruption listener function will run on. Passing `NULL` is equivalent to passing `kCFRunLoopDefaultMode`.
- `inInterruptionListener`: The interruption listener callback function. The application’s audio session object invokes the callback when the session is interrupted and (if the application is still running) when the interruption ends. Can be `NULL`. See [`AudioSessionInterruptionListener`](./audiosessioninterruptionlistener.md).
- `inClientData`: Data that you would like to be passed to your interruption listener callback.

## See Also

### Functions
- [func AudioFileReadPackets(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](./audiofilereadpackets%28_,_,_,_,_,_,_%29.md)
  Reads a fixed duration of audio data from an audio file.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](./audiocomponentgeticon%28_,_%29.md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](./audiocomponentgetlastactivetime%28_%29.md)
  The time at which the application publishing the component was last active.
- [func AudioHardwareServiceAddPropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, AudioObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](./audiohardwareserviceaddpropertylistener%28_,_,_,_%29.md)
  Registers a HAL audio object property listener callback function to be invoked when a specified property changes.
- [func AudioHardwareServiceGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](./audiohardwareservicegetpropertydata%28_,_,_,_,_,_%29.md)
  Gets the value for a specified property.
- [func AudioHardwareServiceGetPropertyDataSize(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!) -> OSStatus](./audiohardwareservicegetpropertydatasize%28_,_,_,_,_%29.md)
  Gets the payload size for a given property.
- [func AudioHardwareServiceHasProperty(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!) -> Bool](./audiohardwareservicehasproperty%28_,_%29.md)
  Queries a HAL audio object about whether or not it has a specified property.
- [func AudioHardwareServiceIsPropertySettable(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](./audiohardwareserviceispropertysettable%28_,_,_%29.md)
  Queries a HAL audio object about whether a specified property is settable.
- [func AudioHardwareServiceRemovePropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, AudioObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](./audiohardwareserviceremovepropertylistener%28_,_,_,_%29.md)
  Unregisters a HAL audio object property listener callback function.
- [func AudioHardwareServiceSetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UInt32, UnsafeRawPointer!) -> OSStatus](./audiohardwareservicesetpropertydata%28_,_,_,_,_,_%29.md)
  Asks a HAL audio object to change the value of a specified property.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](./audiooutputunitgethosticon%28_,_%29.md)
  The host app’s icon.
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](./audiooutputunitpublish%28_,_,_,_%29.md)
  Registers an audio output unit for use by other applications.
- [func AudioSessionAddPropertyListener(AudioSessionPropertyID, AudioSessionPropertyListener!, UnsafeMutableRawPointer!) -> OSStatus](./audiosessionaddpropertylistener%28_,_,_%29.md)
  Adds a property listener callback function to your application’s audio session object.
- [func AudioSessionGetProperty(AudioSessionPropertyID, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](./audiosessiongetproperty%28_,_,_%29.md)
  Gets the value of a specified audio session property.
- [func AudioSessionGetPropertySize(AudioSessionPropertyID, UnsafeMutablePointer<UInt32>!) -> OSStatus](./audiosessiongetpropertysize%28_,_%29.md)
  Gets the size of the value for a specified audio session property.
- [AudioFileCreate](./audiofilecreate.md)
- [AudioFileInitialize](./audiofileinitialize.md)
- [AudioFileOpen](./audiofileopen.md)
- [MusicSequenceLoadSMFDataWithFlags](./musicsequenceloadsmfdatawithflags.md)
- [MusicSequenceLoadSMFWithFlags](./musicsequenceloadsmfwithflags.md)
- [MusicSequenceSaveMIDIFile](./musicsequencesavemidifile.md)
- [MusicSequenceSaveSMFData](./musicsequencesavesmfdata.md)
- [MusicTrackNewExtendedControlEvent](./musictracknewextendedcontrolevent.md)
- [AudioFileComponentCreate](./audiofilecomponentcreate.md)
- [AudioFileComponentDataIsThisFormat](./audiofilecomponentdataisthisformat.md)
- [AudioFileComponentFileIsThisFormat](./audiofilecomponentfileisthisformat.md)
- [AudioFileComponentInitialize](./audiofilecomponentinitialize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiosessioninitialize(_:_:_:_:))*