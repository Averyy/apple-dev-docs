# MIDIThruConnectionSetParams(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Updates a thru connection’s parameters.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIThruConnectionSetParams(_ connection: MIDIThruConnectionRef, _ inConnectionParams: CFData) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `connection`: The connection to update.
- `inConnectionParams`: The connection’s new parameters in a  .

## See Also

- [struct MIDIThruConnectionParams](midithruconnectionparams.md)
  A set of MIDI routings and transformations.
- [func MIDIThruConnectionParamsSize(UnsafePointer<MIDIThruConnectionParams>) -> Int](midithruconnectionparamssize(_:).md)
  Returns the size of a MIDI thru connection parameters object.
- [func MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)](midithruconnectionparamsinitialize(_:).md)
  Initializes a parameters object with its default values.
- [func MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](midithruconnectiongetparams(_:_:).md)
  Returns the thru connection’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionsetparams(_:_:))*