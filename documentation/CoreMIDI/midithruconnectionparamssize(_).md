# MIDIThruConnectionParamsSize(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns the size of a MIDI thru connection parameters object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func MIDIThruConnectionParamsSize(_ ptr: UnsafePointer<MIDIThruConnectionParams>) -> Int
```

```c
static size_t MIDIThruConnectionParamsSize(const MIDIThruConnectionParams *ptr);
```

## Return Value

The connection’s parameter’s size.

## Discussion

This function accounts for variable-length elements in the structure and returns its true size in bytes.

## Parameters

- `ptr`: The parameters pointer.

## See Also

### Configuring Parameters
- [struct MIDIThruConnectionParams](./midithruconnectionparams.md)
  A set of MIDI routings and transformations.
- [func MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)](./midithruconnectionparamsinitialize%28_%29.md)
  Initializes a parameters object with its default values.
- [func MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](./midithruconnectiongetparams%28_,_%29.md)
  Returns the thru connection’s parameters.
- [func MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData) -> OSStatus](./midithruconnectionsetparams%28_,_%29.md)
  Updates a thru connection’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparamssize(_:))*