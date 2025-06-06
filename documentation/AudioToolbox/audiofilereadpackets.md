# AudioFileReadPackets(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Reads a fixed duration of audio data from an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

If you do not need to read a fixed duration of audio data, but rather want to use your memory buffer most efficiently, use [`AudioFileReadPacketData(_:_:_:_:_:_:_:)`](audiofilereadpacketdata(_:_:_:_:_:_:_:).md) instead of this function.

When reading variable bit-rate (VBR) audio data, using this function requires that you allocate more memory than you would for the [`AudioFileReadPacketData(_:_:_:_:_:_:_:)`](audiofilereadpacketdata(_:_:_:_:_:_:_:).md) function. See the descriptions for the `outBuffer` parameter in each of these two functions.

In addition, this function is less efficient than [`AudioFileReadPacketData(_:_:_:_:_:_:_:)`](audiofilereadpacketdata(_:_:_:_:_:_:_:).md) when reading compressed file formats that do not have packet tables, such as MP3 or ADTS. Use this function only when you need to read a fixed duration of audio data, or when you are reading only uncompressed audio.

Audio File Services reads one 32-bit chunk of a file at a time.

## Parameters

- `inAudioFile`: The audio file whose audio packets you want to read.
- `inUseCache`: Set to   to cache the data. Otherwise, set to  .
- `outNumBytes`: On output, the number of bytes actually read.
- `outPacketDescriptions`: This parameter applies only to variable bit-rate data. If the file being read contains constant bit-rate (CBR) data, such as linear PCM, this parameter does not get filled. Pass   if the file’s data format is CBR.
- `inStartingPacket`: The packet index of the first packet you want to read.
- `ioNumPackets`: You will see a difference in the input and output values when this function has reached the end of the file you are reading. In this case, the output value for this parameter is smaller than its input value.
- `outBuffer`: Memory that you allocate to hold the read packets. Determine an appropriate size by multiplying the number of packets requested (in the   parameter) by the maximum (or upper bound for) packet size of the audio file. For uncompressed audio formats, a packet is equal to a frame.

## See Also

- [func AudioFileWritePackets(AudioFileID, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritepackets(_:_:_:_:_:_:_:).md)
  Writes packets of audio data to an audio data file.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](audiocomponentgeticon(_:_:).md)
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
- [func AudioSessionInitialize(CFRunLoop!, CFString!, AudioSessionInterruptionListener!, UnsafeMutableRawPointer!) -> OSStatus](audiosessioninitialize(_:_:_:_:).md)
  Initializes an iOS application’s audio session object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilereadpackets(_:_:_:_:_:_:_:))*