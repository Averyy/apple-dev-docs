# MIDIThruConnectionRef

**Framework**: Core MIDI  
**Kind**: typealias

An opaque reference to a play-through connection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias MIDIThruConnectionRef = MIDIObjectRef
```

## See Also

- [func MIDIThruConnectionCreate(CFString?, CFData, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus](midithruconnectioncreate(_:_:_:).md)
  Creates a MIDI thru connection.
- [func MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus](midithruconnectiondispose(_:).md)
  Disposes a MIDI thru connection.
- [struct MIDIThruConnectionEndpoint](midithruconnectionendpoint.md)
  A source or destination in a MIDI thru connection.
- [Endpoint Configuration](endpoint-configuration.md)
  Values that define the supported endpoint configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionref)*