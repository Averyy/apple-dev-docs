# Deprecated Symbols

**Framework**: Audio Toolbox

Review unsupported symbols and their replacements.

## Topics

### Inter-App Audio
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](audiooutputunitpublish(_:_:_:_:).md)
  Registers an audio output unit for use by other applications.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](audiooutputunitgethosticon(_:_:).md)
  The host app’s icon.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](audiocomponentgeticon(_:_:).md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](audiocomponentgetlastactivetime(_:).md)
  The time at which the application publishing the component was last active.
### Functions
- [func AudioFileReadPackets(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audiofilereadpackets(_:_:_:_:_:_:_:).md)
  Reads a fixed duration of audio data from an audio file.
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
- [func AudioSessionRemovePropertyListener(AudioSessionPropertyID) -> OSStatus](audiosessionremovepropertylistener(_:).md)
  Removes an audio session property listener callback function.
- [func AudioSessionRemovePropertyListenerWithUserData(AudioSessionPropertyID, AudioSessionPropertyListener!, UnsafeMutableRawPointer!) -> OSStatus](audiosessionremovepropertylistenerwithuserdata(_:_:_:).md)
  Removes a property listener callback function from your application’s audio session object.
- [func AudioSessionSetActive(Bool) -> OSStatus](audiosessionsetactive(_:).md)
  Actives or deactivates your application’s audio session.
- [func AudioSessionSetActiveWithFlags(Bool, UInt32) -> OSStatus](audiosessionsetactivewithflags(_:_:).md)
  Activates or deactivates your application’s audio session; provides flags for use by other audio sessions.
- [func AudioSessionSetProperty(AudioSessionPropertyID, UInt32, UnsafeRawPointer!) -> OSStatus](audiosessionsetproperty(_:_:_:).md)
  Sets the value of a specified audio session property.
### Callbacks
- [typealias AudioSessionInterruptionListener](audiosessioninterruptionlistener.md)
  Invoked when an audio interruption in iOS begins or ends.
- [typealias AudioSessionPropertyListener](audiosessionpropertylistener.md)
  Invoked when an audio session property changes in iOS.
### Data Types
- [struct ExtendedControlEvent](extendedcontrolevent.md)
- [typealias MIDIEndpointRef](../CoreMIDI/MIDIEndpointRef.md)
  A MIDI source or destination an entity owns.
- [typealias MagicCookieInfo](magiccookieinfo.md)
  A structure holding magic cookie information.
- [typealias NoteInstanceID](noteinstanceid.md)
- [typealias ReadBytesFDF](readbytesfdf.md)
- [typealias ReadPacketDataFDF](readpacketdatafdf.md)
- [typealias ReadPacketsFDF](readpacketsfdf.md)
- [typealias SetPropertyFDF](setpropertyfdf.md)
- [typealias SetUserDataFDF](setuserdatafdf.md)
- [typealias WriteBytesFDF](writebytesfdf.md)
- [typealias WritePacketsFDF](writepacketsfdf.md)
- [typealias AudioSessionPropertyID](audiosessionpropertyid.md)
  The data type for an audio session property identifier.
### Constants
- [Audio Unit Attenuation Properties](1534112-audio-unit-attenuation-propertie.md)
- [Audio Unit Instrument Errors](1584141-audio-unit-instrument-errors.md)
- [Anonymous](1534019-anonymous.md)
- [Anonymous](1534074-anonymous.md)
- [Audio Graph Errors](1537630-audio-graph-errors.md)
- [Audio Converter Property ID](1624333-audio-converter-property-id.md)
- [Anonymous](1621044-anonymous.md)
- [Anonymous](1618426-anonymous.md)
- [Anonymous](1618742-anonymous.md)
- [Anonymous](1619479-anonymous.md)
- [Anonymous](1619504-anonymous.md)
- [Anonymous](1533960-anonymous.md)
- [Anonymous](1534225-anonymous.md)
- [Music Device Properties](1534089-music-device-properties.md)
- [3D Mixer Audio Unit Properties](1534063-3d_mixer_audio_unit_properties.md)
  Properties for the Apple 3D Mixer audio unit.
- [var kAudioSession_AudioRouteChangeKey_OldRoute: String](kaudiosession_audioroutechangekey_oldroute.md)
- [var AU_SUPPORT_INTERAPP_AUDIO: Int32](au_support_interapp_audio.md)
- [Hardware Codec Capabilities](1620452-hardware-codec-capabilities.md)
  A constant to determine which hardware codecs can be used.
- [Deprecated Audio Codec Properties](1494107-deprecated-audio-codec-propertie.md)
- [Deprecated Constants Used With kAudioCodecBitRateFormat](1494081-deprecated-constants-used-with-k.md)
- [Deprecated Constants Used With kAudioCodecOutputPrecedence](1494070-deprecated-constants-used-with-k.md)
- [Deprecated Constants Used With kAudioSettings_Hint](1494142-deprecated-constants-used-with-k.md)
- [Deprecated Audio Session Categories](1618459-deprecated-audio-session-categor.md)
  Deprecated category identifiers for audio sessions. Do not use for new development.
### Audio Graphs
- [Audio Unit Processing Graph Services](audio-unit-processing-graph-services.md)
  Audio Unit Processing Graph Services provide interfaces for representing a set of audio units, connections between their inputs and outputs, and callbacks used to provide inputs. It also enables the embedding of sub (or child) processing graphs within parent graphs to allow for a logical organization of parts of an overall signal chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/deprecated-symbols)*