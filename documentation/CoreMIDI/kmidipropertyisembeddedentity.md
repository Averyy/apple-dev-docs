# kMIDIPropertyIsEmbeddedEntity

**Framework**: Core MIDI  
**Kind**: var

A Boolean value that indicates whether this entity or endpoint has external MIDI connections.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyIsEmbeddedEntity: CFString
```

## See Also

- [let kMIDIPropertyCanRoute: CFString](kmidipropertycanroute.md)
  A Boolean value that indicates whether the device or entity can route messages to or from external MIDI devices.
- [let kMIDIPropertyIsBroadcast: CFString](kmidipropertyisbroadcast.md)
  A Boolean value that indicates whether the endpoint broadcasts messages to all of the other endpoints in the device.
- [let kMIDIPropertyConnectionUniqueID: CFString](kmidipropertyconnectionuniqueid.md)
  The unique identifier of an external device attached to this connection.
- [let kMIDIPropertySingleRealtimeEntity: CFString](kmidipropertysinglerealtimeentity.md)
  The 0-based index of the entity on which incoming real-time messages from the device appear to have originated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyisembeddedentity)*