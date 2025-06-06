# kMIDIPropertyConnectionUniqueID

**Framework**: Core MIDI  
**Kind**: var

The unique identifier of an external device attached to this connection.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyConnectionUniqueID: CFString
```

#### Discussion

The value provided may be an integer. To indicate that a driver connects to multiple external objects, pass the array of big-endian `SInt32` values as a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object.

The property is nonexistent or 0 if there’s no connection.

## See Also

- [let kMIDIPropertyCanRoute: CFString](kmidipropertycanroute.md)
  A Boolean value that indicates whether the device or entity can route messages to or from external MIDI devices.
- [let kMIDIPropertyIsBroadcast: CFString](kmidipropertyisbroadcast.md)
  A Boolean value that indicates whether the endpoint broadcasts messages to all of the other endpoints in the device.
- [let kMIDIPropertyIsEmbeddedEntity: CFString](kmidipropertyisembeddedentity.md)
  A Boolean value that indicates whether this entity or endpoint has external MIDI connections.
- [let kMIDIPropertySingleRealtimeEntity: CFString](kmidipropertysinglerealtimeentity.md)
  The 0-based index of the entity on which incoming real-time messages from the device appear to have originated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyconnectionuniqueid)*