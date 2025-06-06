# MIDIThruConnectionFind(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Finds the persistent thru connections for the specified client.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString, _ outConnectionList: UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `inPersistentOwnerID`: The identifier of the owning object.
- `outConnectionList`: On successful return, a   that contains an array of MIDI thru connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionfind(_:_:))*