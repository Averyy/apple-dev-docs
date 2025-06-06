# MIDIThruConnectionDispose(_:)

**Framework**: Core MIDI  
**Kind**: func

Disposes a MIDI thru connection.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIThruConnectionDispose(_ connection: MIDIThruConnectionRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `connection`: The connection to dispose.

## See Also

- [func MIDIThruConnectionCreate(CFString?, CFData, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus](midithruconnectioncreate(_:_:_:).md)
  Creates a MIDI thru connection.
- [typealias MIDIThruConnectionRef](midithruconnectionref.md)
  An opaque reference to a play-through connection.
- [struct MIDIThruConnectionEndpoint](midithruconnectionendpoint.md)
  A source or destination in a MIDI thru connection.
- [Endpoint Configuration](endpoint-configuration.md)
  Values that define the supported endpoint configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectiondispose(_:))*