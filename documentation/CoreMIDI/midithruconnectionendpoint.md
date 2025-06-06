# MIDIThruConnectionEndpoint

**Framework**: Core MIDI  
**Kind**: struct

A source or destination in a MIDI thru connection.

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
struct MIDIThruConnectionEndpoint
```

#### Overview

Set the endpoint’s [`uniqueID`](midithruconnectionendpoint/uniqueid.md) to 0 if the endpoint exists and you’re passing its [`endpointRef`](midithruconnectionendpoint/endpointref.md). When retrieving a connection from Core MIDI, its [`endpointRef`](midithruconnectionendpoint/endpointref.md) may be `NULL` if it doesn’t exist, but the [`uniqueID`](midithruconnectionendpoint/uniqueid.md) is always non-zero.

## Topics

### Configuring an Endpoint
- [var uniqueID: MIDIUniqueID](midithruconnectionendpoint/uniqueid.md)
  The connection’s unique identifier.
- [var endpointRef: MIDIEndpointRef](midithruconnectionendpoint/endpointref.md)
  The endpoint reference.
### Initializers
- [init()](midithruconnectionendpoint/init.md)
- [init(endpointRef: MIDIEndpointRef, uniqueID: MIDIUniqueID)](midithruconnectionendpoint/init(endpointref:uniqueid:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func MIDIThruConnectionCreate(CFString?, CFData, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus](midithruconnectioncreate(_:_:_:).md)
  Creates a MIDI thru connection.
- [func MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus](midithruconnectiondispose(_:).md)
  Disposes a MIDI thru connection.
- [typealias MIDIThruConnectionRef](midithruconnectionref.md)
  An opaque reference to a play-through connection.
- [Endpoint Configuration](endpoint-configuration.md)
  Values that define the supported endpoint configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionendpoint)*