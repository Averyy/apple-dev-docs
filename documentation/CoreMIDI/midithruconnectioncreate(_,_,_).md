# MIDIThruConnectionCreate(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Creates a MIDI thru connection.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIThruConnectionCreate(_ inPersistentOwnerID: CFString?, _ inConnectionParams: CFData, _ outConnection: UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus
```

```c
extern OSStatus MIDIThruConnectionCreate(CFStringRef inPersistentOwnerID, CFDataRef inConnectionParams, MIDIThruConnectionRef *outConnection);
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `inPersistentOwnerID`: A unique identifier of the owning object, such as `com.mycompany.MyApp`. If you pass `NULL`, the client owns the connection and it’s automatically disposed with the client.
- `inConnectionParams`: A [`MIDIThruConnectionParams`](./midithruconnectionparams.md) object that’s contained in a [`CFData`](../CoreFoundation/cfdata.md).
- `outConnection`: On successful return, a reference to the newly created connection.

## See Also

### Managing Connections
- [func MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus](./midithruconnectiondispose%28_%29.md)
  Disposes a MIDI thru connection.
- [typealias MIDIThruConnectionRef](./midithruconnectionref.md)
  An opaque reference to a play-through connection.
- [struct MIDIThruConnectionEndpoint](./midithruconnectionendpoint.md)
  A source or destination in a MIDI thru connection.
- [Endpoint Configuration](./endpoint-configuration.md)
  Values that define the supported endpoint configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectioncreate(_:_:_:))*