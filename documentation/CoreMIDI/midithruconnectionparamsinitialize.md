# MIDIThruConnectionParamsInitialize(_:)

**Framework**: Core MIDI  
**Kind**: func

Initializes a parameters object with its default values.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIThruConnectionParamsInitialize(_ inConnectionParams: UnsafeMutablePointer<MIDIThruConnectionParams>)
```

#### Discussion

This is a convenience function that fills the connection structure with default values. Set the source and destination to create a simple, unmodified thru connection.

## Parameters

- `inConnectionParams`: The parameters to initialize.

## See Also

- [struct MIDIThruConnectionParams](midithruconnectionparams.md)
  A set of MIDI routings and transformations.
- [func MIDIThruConnectionParamsSize(UnsafePointer<MIDIThruConnectionParams>) -> Int](midithruconnectionparamssize(_:).md)
  Returns the size of a MIDI thru connection parameters object.
- [func MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](midithruconnectiongetparams(_:_:).md)
  Returns the thru connection’s parameters.
- [func MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData) -> OSStatus](midithruconnectionsetparams(_:_:).md)
  Updates a thru connection’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparamsinitialize(_:))*