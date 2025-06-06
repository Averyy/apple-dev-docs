# CFNetDiagnosticDiagnoseProblemInteractively(_:)

**Framework**: CFNetwork  
**Kind**: func

Opens a Network Diagnostics window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetDiagnosticDiagnoseProblemInteractively(_ details: CFNetDiagnostic) -> CFNetDiagnosticStatus
```

#### Return Value

`CFNetDiagnosticNoErr` if no error occurred, or `CFNetDiagnosticErr` if an error occurred that prevented this call from completing successfully.

#### Discussion

This function opens the Network Diagnostics window and returns immediately once the window is open.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `details`: A network diagnostics object, created by   or  , for which the window is to be opened.

## See Also

- [class CFNetDiagnostic](cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithstreams(_:_:_:).md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithurl(_:_:).md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](cfnetdiagnosticsetname(_:_:).md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticdiagnoseprobleminteractively(_:))*