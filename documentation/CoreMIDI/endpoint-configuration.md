# Endpoint Configuration

**Framework**: Core MIDI

Values that define the supported endpoint configurations.

## Topics

### Configuration Constants
- [var kMIDIThruConnection_MaxEndpoints: Int](kmidithruconnection_maxendpoints.md)
  The maximum number of endpoints for this connection.

## See Also

- [func MIDIThruConnectionCreate(CFString?, CFData, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus](midithruconnectioncreate(_:_:_:).md)
  Creates a MIDI thru connection.
- [func MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus](midithruconnectiondispose(_:).md)
  Disposes a MIDI thru connection.
- [typealias MIDIThruConnectionRef](midithruconnectionref.md)
  An opaque reference to a play-through connection.
- [struct MIDIThruConnectionEndpoint](midithruconnectionendpoint.md)
  A source or destination in a MIDI thru connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/endpoint-configuration)*