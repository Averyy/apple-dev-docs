# MIDIThruConnectionGetParams(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Returns the thru connection’s parameters.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIThruConnectionGetParams(_ connection: MIDIThruConnectionRef, _ outConnectionParams: UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

The returned object contains a [`MIDIThruConnectionParams`](midithruconnectionparams.md) structure. The caller is responsible for releasing it.

## Parameters

- `connection`: The connection to dispose.
- `outConnectionParams`: On successful return, the connection’s parameters in a  .

## See Also

- [struct MIDIThruConnectionParams](midithruconnectionparams.md)
  A set of MIDI routings and transformations.
- [func MIDIThruConnectionParamsSize(UnsafePointer<MIDIThruConnectionParams>) -> Int](midithruconnectionparamssize(_:).md)
  Returns the size of a MIDI thru connection parameters object.
- [func MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)](midithruconnectionparamsinitialize(_:).md)
  Initializes a parameters object with its default values.
- [func MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData) -> OSStatus](midithruconnectionsetparams(_:_:).md)
  Updates a thru connection’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectiongetparams(_:_:))*