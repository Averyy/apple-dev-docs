# MIDI Object Properties

**Framework**: Core MIDI

Configure the properties of MIDI objects.

## Topics

### Identification
- [let kMIDIPropertyName: CFString](kmidipropertyname.md)
  A name for a device, entity, or endpoint.
- [let kMIDIPropertyModel: CFString](kmidipropertymodel.md)
  The model name of a device or endpoint.
- [let kMIDIPropertyManufacturer: CFString](kmidipropertymanufacturer.md)
  The manufacturer name of a device or endpoint.
- [let kMIDIPropertyUniqueID: CFString](kmidipropertyuniqueid.md)
  The unique identifier of a device, entity, or, endpoint.
- [let kMIDIPropertyDeviceID: CFString](kmidipropertydeviceid.md)
  The user-visible System Exclusive (SysEx) identifier of a device or entity.
### Capabilities
- [let kMIDIPropertySupportsMMC: CFString](kmidipropertysupportsmmc.md)
  A Boolean value that indicates whether the device or entity implements the MIDI Machine Control portion of the MIDI specification.
- [let kMIDIPropertySupportsGeneralMIDI: CFString](kmidipropertysupportsgeneralmidi.md)
  A Boolean value that indicates whether the device or entity implements the General MIDI specification.
- [let kMIDIPropertySupportsShowControl: CFString](kmidipropertysupportsshowcontrol.md)
  A Boolean value that indicates whether the device implements the MIDI Show Control specification.
### Configuration
- [let kMIDIPropertyNameConfigurationDictionary: CFString](kmidipropertynameconfigurationdictionary.md)
  The device’s current patch, note, and control name values in MIDINameDocument XML format.
- [let kMIDIPropertyMaxSysExSpeed: CFString](kmidipropertymaxsysexspeed.md)
  The maximum rate, in bytes per second, at which the system may reliably send System Exclusive (SysEx) messages to this object.
- [let kMIDIPropertyDriverDeviceEditorApp: CFString](kmidipropertydriverdeviceeditorapp.md)
  The full path to an app on the system that configures driver-owned devices.
- [let kMIDIPropertyNameConfiguration: CFString](kmidipropertynameconfiguration.md)
  An XML representation of the device’s current patch, note, and control name values.
### Presentation
- [let kMIDIPropertyImage: CFString](kmidipropertyimage.md)
  The full path to a device icon on the system.
- [let kMIDIPropertyDisplayName: CFString](kmidipropertydisplayname.md)
  The user-visible name for an endpoint that combines the device and endpoint names.
### Audio
- [let kMIDIPropertyPanDisruptsStereo: CFString](kmidipropertypandisruptsstereo.md)
  A Boolean value that indicates whether the MIDI pan messages sent to the device or entity cause undesirable effects when playing stereo sounds.
### Protocols
- [let kMIDIPropertyProtocolID: CFString](kmidipropertyprotocolid.md)
  The native protocol in which the endpoint communicates.
### Timing
- [let kMIDIPropertyTransmitsMTC: CFString](kmidipropertytransmitsmtc.md)
  A Boolean value that indicates whether the device or entity transmits MIDI Time Code messages.
- [let kMIDIPropertyReceivesMTC: CFString](kmidipropertyreceivesmtc.md)
  A Boolean value that indicates whether the device or entity responds to MIDI Time Code messages.
- [let kMIDIPropertyTransmitsClock: CFString](kmidipropertytransmitsclock.md)
  A Boolean value that indicates whether the device or entity transmits MIDI beat clock messages.
- [let kMIDIPropertyReceivesClock: CFString](kmidipropertyreceivesclock.md)
  A Boolean value that indicates whether the device or entity responds to MIDI beat clock messages.
- [let kMIDIPropertyAdvanceScheduleTimeMuSec: CFString](kmidipropertyadvancescheduletimemusec.md)
  The recommended number of microseconds in advance that clients should schedule output.
### Roles
- [let kMIDIPropertyIsMixer: CFString](kmidipropertyismixer.md)
  A Boolean value that indicates whether the device or entity mixes external audio signals.
- [let kMIDIPropertyIsSampler: CFString](kmidipropertyissampler.md)
  A Boolean value that indicates whether the device or entity plays audio samples in response to MIDI note messages.
- [let kMIDIPropertyIsEffectUnit: CFString](kmidipropertyiseffectunit.md)
  A Boolean value that indicates whether the device or entity primarily acts as a MIDI-controlled audio effect.
- [let kMIDIPropertyIsDrumMachine: CFString](kmidipropertyisdrummachine.md)
  A Boolean value that indicates whether the device or entity’s samples aren’t transposable, as with a drum kit.
### Status
- [let kMIDIPropertyOffline: CFString](kmidipropertyoffline.md)
  A Boolean value that indicates whether the object is offline.
- [let kMIDIPropertyPrivate: CFString](kmidipropertyprivate.md)
  A Boolean value that indicates whether the system hides an endpoint from other clients.
### Drivers
- [let kMIDIPropertyDriverOwner: CFString](kmidipropertydriverowner.md)
  The name of the driver that owns a device, entity, or endpoint.
- [let kMIDIPropertyDriverVersion: CFString](kmidipropertydriverversion.md)
  The version of the driver that owns a device, entity, or endpoint.
### Connections
- [let kMIDIPropertyCanRoute: CFString](kmidipropertycanroute.md)
  A Boolean value that indicates whether the device or entity can route messages to or from external MIDI devices.
- [let kMIDIPropertyIsBroadcast: CFString](kmidipropertyisbroadcast.md)
  A Boolean value that indicates whether the endpoint broadcasts messages to all of the other endpoints in the device.
- [let kMIDIPropertyConnectionUniqueID: CFString](kmidipropertyconnectionuniqueid.md)
  The unique identifier of an external device attached to this connection.
- [let kMIDIPropertyIsEmbeddedEntity: CFString](kmidipropertyisembeddedentity.md)
  A Boolean value that indicates whether this entity or endpoint has external MIDI connections.
- [let kMIDIPropertySingleRealtimeEntity: CFString](kmidipropertysinglerealtimeentity.md)
  The 0-based index of the entity on which incoming real-time messages from the device appear to have originated.
### Channels
- [let kMIDIPropertyReceiveChannels: CFString](kmidipropertyreceivechannels.md)
  The bitmap of channels on which the object receives messages.
- [let kMIDIPropertyTransmitChannels: CFString](kmidipropertytransmitchannels.md)
  The bitmap of channels on which the object transmits messages.
- [let kMIDIPropertyMaxReceiveChannels: CFString](kmidipropertymaxreceivechannels.md)
  The maximum number of MIDI channels on which a device may simultaneously receive channel messages.
- [let kMIDIPropertyMaxTransmitChannels: CFString](kmidipropertymaxtransmitchannels.md)
  The maximum number of MIDI channels on which a device may simultaneously transmit channel messages.
### Banks
- [let kMIDIPropertyReceivesBankSelectLSB: CFString](kmidipropertyreceivesbankselectlsb.md)
  A Boolean value that indicates whether the device or entity responds to MIDI bank select LSB messages.
- [let kMIDIPropertyReceivesBankSelectMSB: CFString](kmidipropertyreceivesbankselectmsb.md)
  A Boolean value that indicates whether the device or entity responds to MIDI bank select MSB messages.
- [let kMIDIPropertyTransmitsBankSelectLSB: CFString](kmidipropertytransmitsbankselectlsb.md)
  A Boolean value that indicates whether the device or entity transmits MIDI bank select LSB messages.
- [let kMIDIPropertyTransmitsBankSelectMSB: CFString](kmidipropertytransmitsbankselectmsb.md)
  A Boolean value that indicates whether the device or entity transmits MIDI bank select MSB messages.
### Notes
- [let kMIDIPropertyReceivesNotes: CFString](kmidipropertyreceivesnotes.md)
  A Boolean value that indicates whether the device or entity responds to MIDI Note On messages.
- [let kMIDIPropertyTransmitsNotes: CFString](kmidipropertytransmitsnotes.md)
  A Boolean value that indicates whether the device or entity transmits MIDI note messages.
### Program Changes
- [let kMIDIPropertyReceivesProgramChanges: CFString](kmidipropertyreceivesprogramchanges.md)
  A Boolean value that indicates whether the device or entity responds to MIDI Program Change messages.
- [let kMIDIPropertyTransmitsProgramChanges: CFString](kmidipropertytransmitsprogramchanges.md)
  A Boolean value that indicates whether the device or entity transmits MIDI Program Change messages.
### Property Accessors
- [func MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Bool) -> OSStatus](midiobjectgetproperties(_:_:_:).md)
  Returns all properties of an object.
- [func MIDIObjectRemoveProperty(MIDIObjectRef, CFString) -> OSStatus](midiobjectremoveproperty(_:_:).md)
  Removes an object’s property.
- [func MIDIObjectGetStringProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](midiobjectgetstringproperty(_:_:_:).md)
  Gets an object’s string-type property.
- [func MIDIObjectSetStringProperty(MIDIObjectRef, CFString, CFString) -> OSStatus](midiobjectsetstringproperty(_:_:_:).md)
  Sets an object’s string-type property.
- [func MIDIObjectGetIntegerProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Int32>) -> OSStatus](midiobjectgetintegerproperty(_:_:_:).md)
  Gets an object’s integer-type property.
- [func MIDIObjectSetIntegerProperty(MIDIObjectRef, CFString, Int32) -> OSStatus](midiobjectsetintegerproperty(_:_:_:).md)
  Sets an object’s integer-type property.
- [func MIDIObjectGetDataProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](midiobjectgetdataproperty(_:_:_:).md)
  Gets an object’s data-type property.
- [func MIDIObjectSetDataProperty(MIDIObjectRef, CFString, CFData) -> OSStatus](midiobjectsetdataproperty(_:_:_:).md)
  Sets an object’s data-type property.
- [func MIDIObjectGetDictionaryProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](midiobjectgetdictionaryproperty(_:_:_:).md)
  Gets an object’s dictionary-type property.
- [func MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString, CFDictionary) -> OSStatus](midiobjectsetdictionaryproperty(_:_:_:).md)
  Sets an object’s dictionary-type property.
### Notifications
- [struct MIDIObjectAddRemoveNotification](midiobjectaddremovenotification.md)
  A message that describes the addition or removal of an object.
- [struct MIDIObjectPropertyChangeNotification](midiobjectpropertychangenotification.md)
  A message that describes the change to an object property.

## See Also

- [func MIDIObjectFindByUniqueID(MIDIUniqueID, UnsafeMutablePointer<MIDIObjectRef>?, UnsafeMutablePointer<MIDIObjectType>?) -> OSStatus](midiobjectfindbyuniqueid(_:_:_:).md)
  Locates a device, entity, or endpoint by its unique identifier.
- [typealias MIDIObjectRef](midiobjectref.md)
  The common base class for many of the framework’s objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-object-properties)*