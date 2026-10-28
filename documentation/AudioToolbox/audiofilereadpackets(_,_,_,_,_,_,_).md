# AudioFileReadPackets(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Reads a fixed duration of audio data from an audio file.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: no longer supported

## Declaration

```swift
func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer?) -> OSStatus
```

```c
extern OSStatus AudioFileReadPackets(AudioFileID inAudioFile, Boolean inUseCache, UInt32 *outNumBytes, AudioStreamPacketDescription *outPacketDescriptions, SInt64 inStartingPacket, UInt32 *ioNumPackets, void *outBuffer);
```

## Return Value

A result code. See Result Codes.

## Discussion

If you do not need to read a fixed duration of audio data, but rather want to use your memory buffer most efficiently, use [`AudioFileReadPacketData(_:_:_:_:_:_:_:)`](./audiofilereadpacketdata%28_,_,_,_,_,_,_%29.md) instead of this function.

When reading variable bit-rate (VBR) audio data, using this function requires that you allocate more memory than you would for the [`AudioFileReadPacketData(_:_:_:_:_:_:_:)`](./audiofilereadpacketdata%28_,_,_,_,_,_,_%29.md) function. See the descriptions for the `outBuffer` parameter in each of these two functions.

In addition, this function is less efficient than [`AudioFileReadPacketData(_:_:_:_:_:_:_:)`](./audiofilereadpacketdata%28_,_,_,_,_,_,_%29.md) when reading compressed file formats that do not have packet tables, such as MP3 or ADTS. Use this function only when you need to read a fixed duration of audio data, or when you are reading only uncompressed audio.

Audio File Services reads one 32-bit chunk of a file at a time.

## Parameters

- `inAudioFile`: The audio file whose audio packets you want to read.
- `inUseCache`: Set to `true` to cache the data. Otherwise, set to `false`.
- `outNumBytes`: On output, the number of bytes actually read.
- `outPacketDescriptions`: On output, an array of packet descriptions for the packets that were read. The array that you pass must be large enough to accommodate descriptions for the number of packets requested in the `ioNumPackets` parameter.

  This parameter applies only to variable bit-rate data. If the file being read contains constant bit-rate (CBR) data, such as linear PCM, this parameter does not get filled. Pass `NULL` if the file’s data format is CBR.
- `inStartingPacket`: The packet index of the first packet you want to read.
- `ioNumPackets`: On input, the number of packets to read. On output, the number of packets actually read.

  You will see a difference in the input and output values when this function has reached the end of the file you are reading. In this case, the output value for this parameter is smaller than its input value.
- `outBuffer`: Memory that you allocate to hold the read packets. Determine an appropriate size by multiplying the number of packets requested (in the `ioNumPackets` parameter) by the maximum (or upper bound for) packet size of the audio file. For uncompressed audio formats, a packet is equal to a frame.

## See Also

### Related Documentation
- [func AudioFileWritePackets(AudioFileID, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilewritepackets%28_,_,_,_,_,_,_%29.md)
  Writes packets of audio data to an audio data file.
### Functions
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
- [func AudioSessionInitialize(CFRunLoop!, CFString!, AudioSessionInterruptionListener!, UnsafeMutableRawPointer!) -> OSStatus](./audiosessioninitialize%28_,_,_,_%29.md)
  Initializes an iOS application’s audio session object.
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
- [AudioFileComponentOpenFile](./audiofilecomponentopenfile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilereadpackets(_:_:_:_:_:_:_:))*