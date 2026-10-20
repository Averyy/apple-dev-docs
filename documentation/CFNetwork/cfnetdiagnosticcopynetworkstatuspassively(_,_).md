# CFNetDiagnosticCopyNetworkStatusPassively(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Gets a network status value.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus
```

```c
extern CFNetDiagnosticStatus CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnosticRef details, CFStringRef*description);
```

#### Return Value

A network status value.

#### Discussion

This function returns a status value that can be used to display basic information about the connection, and optionally gets a localized string containing a description of the current network status.

This function is guaranteed not to generate network activity.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `details`: CFNetDiagnosticRef, created by [`CFNetDiagnosticCreateWithStreams(_:_:_:)`](./cfnetdiagnosticcreatewithstreams%28_,_,_%29.md) or [`CFNetDiagnosticCreateWithURL(_:_:)`](./cfnetdiagnosticcreatewithurl%28_,_%29.md), for which the Network Diagnostics status is to be obtained.
- `description`: If not `NULL`, upon return contains a localized string containing a description of the current network status. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Network Diagnostics
- [class CFNetDiagnostic](./cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](./cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](./cfnetdiagnosticcreatewithstreams%28_,_,_%29.md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](./cfnetdiagnosticcreatewithurl%28_,_%29.md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](./cfnetdiagnosticdiagnoseprobleminteractively%28_%29.md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](./cfnetdiagnosticsetname%28_,_%29.md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcopynetworkstatuspassively(_:_:))*