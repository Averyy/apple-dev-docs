# CFNetDiagnosticDiagnoseProblemInteractively(_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Opens a Network Diagnostics window.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func CFNetDiagnosticDiagnoseProblemInteractively(_ details: CFNetDiagnostic) -> CFNetDiagnosticStatus
```

```c
extern CFNetDiagnosticStatus CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnosticRef details);
```

## Return Value

`CFNetDiagnosticNoErr` if no error occurred, or `CFNetDiagnosticErr` if an error occurred that prevented this call from completing successfully.

## Discussion

This function opens the Network Diagnostics window and returns immediately once the window is open.

### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `details`: A network diagnostics object, created by [`CFNetDiagnosticCreateWithStreams(_:_:_:)`](./cfnetdiagnosticcreatewithstreams%28_,_,_%29.md) or [`CFNetDiagnosticCreateWithURL(_:_:)`](./cfnetdiagnosticcreatewithurl%28_,_%29.md), for which the window is to be opened.

## See Also

### Network Diagnostics
- [class CFNetDiagnostic](./cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](./cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](./cfnetdiagnosticcopynetworkstatuspassively%28_,_%29.md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](./cfnetdiagnosticcreatewithstreams%28_,_,_%29.md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](./cfnetdiagnosticcreatewithurl%28_,_%29.md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](./cfnetdiagnosticsetname%28_,_%29.md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticdiagnoseprobleminteractively(_:))*