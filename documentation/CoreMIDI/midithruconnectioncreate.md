# MIDIThruConnectionCreate(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

An `OSStatus` result code.

## Parameters

- `inPersistentOwnerID`: A unique identifier of the owning object, such as  . If you pass  , the client owns the connection and it’s automatically disposed with the client.
- `inConnectionParams`: A   object that’s contained in a  .
- `outConnection`: On successful return, a reference to the newly created connection.

## See Also

- [func MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus](midithruconnectiondispose(_:).md)
  Disposes a MIDI thru connection.
- [typealias MIDIThruConnectionRef](midithruconnectionref.md)
  An opaque reference to a play-through connection.
- [struct MIDIThruConnectionEndpoint](midithruconnectionendpoint.md)
  A source or destination in a MIDI thru connection.
- [Endpoint Configuration](endpoint-configuration.md)
  Values that define the supported endpoint configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectioncreate(_:_:_:))*