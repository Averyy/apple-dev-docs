# Deprecated Symbols

**Framework**: Audio Toolbox  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Inter-App Audio
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](./audiooutputunitpublish%28_,_,_,_%29.md)
  Registers an audio output unit for use by other applications.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](./audiooutputunitgethosticon%28_,_%29.md)
  The host app’s icon.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](./audiocomponentgeticon%28_,_%29.md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](./audiocomponentgetlastactivetime%28_%29.md)
  The time at which the application publishing the component was last active.
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
- [func AudioSessionInitialize(CFRunLoop!, CFString!, AudioSessionInterruptionListener!, UnsafeMutableRawPointer!) -> OSStatus](./audiosessioninitialize%28_,_,_,_%29.md)
  Initializes an iOS application’s audio session object.
- [func AudioSessionRemovePropertyListener(AudioSessionPropertyID) -> OSStatus](./audiosessionremovepropertylistener%28_%29.md)
  Removes an audio session property listener callback function.
- [func AudioSessionRemovePropertyListenerWithUserData(AudioSessionPropertyID, AudioSessionPropertyListener!, UnsafeMutableRawPointer!) -> OSStatus](./audiosessionremovepropertylistenerwithuserdata%28_,_,_%29.md)
  Removes a property listener callback function from your application’s audio session object.
- [func AudioSessionSetActive(Bool) -> OSStatus](./audiosessionsetactive%28_%29.md)
  Actives or deactivates your application’s audio session.
- [func AudioSessionSetActiveWithFlags(Bool, UInt32) -> OSStatus](./audiosessionsetactivewithflags%28_,_%29.md)
  Activates or deactivates your application’s audio session; provides flags for use by other audio sessions.
- [func AudioSessionSetProperty(AudioSessionPropertyID, UInt32, UnsafeRawPointer!) -> OSStatus](./audiosessionsetproperty%28_,_,_%29.md)
  Sets the value of a specified audio session property.
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
- [MusicDevicePrepareInstrument](./musicdeviceprepareinstrument.md)
- [MusicDeviceReleaseInstrument](./musicdevicereleaseinstrument.md)
### Callbacks
- [typealias AudioSessionInterruptionListener](./audiosessioninterruptionlistener.md)
  Invoked when an audio interruption in iOS begins or ends.
- [typealias AudioSessionPropertyListener](./audiosessionpropertylistener.md)
  Invoked when an audio session property changes in iOS.
### Data Types
- [struct ExtendedControlEvent](./extendedcontrolevent.md)
- [typealias MIDIEndpointRef](../CoreMIDI/midiendpointref.md)
  A MIDI source or destination an entity owns.
- [typealias MagicCookieInfo](./magiccookieinfo.md)
  A structure holding magic cookie information.
- [typealias NoteInstanceID](./noteinstanceid.md)
- [typealias ReadBytesFDF](./readbytesfdf.md)
- [typealias ReadPacketDataFDF](./readpacketdatafdf.md)
- [typealias ReadPacketsFDF](./readpacketsfdf.md)
- [typealias SetPropertyFDF](./setpropertyfdf.md)
- [typealias SetUserDataFDF](./setuserdatafdf.md)
- [typealias WriteBytesFDF](./writebytesfdf.md)
- [typealias WritePacketsFDF](./writepacketsfdf.md)
- [typealias AudioSessionPropertyID](./audiosessionpropertyid.md)
  The data type for an audio session property identifier.
### Constants
- [Audio Unit Attenuation Properties](./api-1534112-audio-unit-attenuation-propertie.md)
- [Audio Unit Instrument Errors](./api-1584141-audio-unit-instrument-errors.md)
- [Anonymous](./api-1534019-anonymous.md)
- [Anonymous](./api-1534074-anonymous.md)
- [Audio Graph Errors](./api-1537630-audio-graph-errors.md)
- [Audio Converter Property ID](./api-1624333-audio-converter-property-id.md)
- [Anonymous](./api-1621044-anonymous.md)
- [Anonymous](./api-1618426-anonymous.md)
- [Anonymous](./api-1618742-anonymous.md)
- [Anonymous](./api-1619479-anonymous.md)
- [Anonymous](./api-1619504-anonymous.md)
- [Anonymous](./api-1533960-anonymous.md)
- [Anonymous](./api-1534225-anonymous.md)
- [Music Device Properties](./api-1534089-music-device-properties.md)
- [3D Mixer Audio Unit Properties](./api-1534063-3d_mixer_audio_unit_properties.md)
  Properties for the Apple 3D Mixer audio unit.
- [var kAudioSession_AudioRouteChangeKey_OldRoute: String](./kaudiosession_audioroutechangekey_oldroute.md)
- [var AU_SUPPORT_INTERAPP_AUDIO: Int32](./au_support_interapp_audio.md)
- [Hardware Codec Capabilities](./api-1620452-hardware-codec-capabilities.md)
  A constant to determine which hardware codecs can be used.
- [Deprecated Audio Codec Properties](./api-1494107-deprecated-audio-codec-propertie.md)
- [Deprecated Constants Used With kAudioCodecBitRateFormat](./api-1494081-deprecated-constants-used-with-k.md)
- [Deprecated Constants Used With kAudioCodecOutputPrecedence](./api-1494070-deprecated-constants-used-with-k.md)
- [Deprecated Constants Used With kAudioSettings_Hint](./api-1494142-deprecated-constants-used-with-k.md)
- [Deprecated Audio Session Categories](./api-1618459-deprecated-audio-session-categor.md)
  Deprecated category identifiers for audio sessions. Do not use for new development.
### Audio Graphs
- [Audio Unit Processing Graph Services](./audio-unit-processing-graph-services.md)
  Audio Unit Processing Graph Services provide interfaces for representing a set of audio units, connections between their inputs and outputs, and callbacks used to provide inputs. It also enables the embedding of sub (or child) processing graphs within parent graphs to allow for a logical organization of parts of an overall signal chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/deprecated-symbols)*