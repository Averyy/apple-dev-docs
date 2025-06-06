# MIDIThruConnectionParamsSize(_:)

**Framework**: Core MIDI  
**Kind**: func

Returns the size of a MIDI thru connection parameters object.

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
func MIDIThruConnectionParamsSize(_ ptr: UnsafePointer<MIDIThruConnectionParams>) -> Int
```

#### Return Value

The connection’s parameter’s size.

#### Discussion

This function accounts for variable-length elements in the structure and returns its true size in bytes.

## Parameters

- `ptr`: The parameters pointer.

## See Also

- [struct MIDIThruConnectionParams](midithruconnectionparams.md)
  A set of MIDI routings and transformations.
- [func MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)](midithruconnectionparamsinitialize(_:).md)
  Initializes a parameters object with its default values.
- [func MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](midithruconnectiongetparams(_:_:).md)
  Returns the thru connection’s parameters.
- [func MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData) -> OSStatus](midithruconnectionsetparams(_:_:).md)
  Updates a thru connection’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparamssize(_:))*