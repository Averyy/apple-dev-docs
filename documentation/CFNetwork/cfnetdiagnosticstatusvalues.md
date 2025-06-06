# CFNetDiagnosticStatusValues

**Framework**: CFNetwork  
**Kind**: enum

Constants for diagnostic status values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum CFNetDiagnosticStatusValues
```

#### Overview

Diagnostic status values are returned by [`CFNetDiagnosticDiagnoseProblemInteractively(_:)`](cfnetdiagnosticdiagnoseprobleminteractively(_:).md) and [`CFNetDiagnosticCopyNetworkStatusPassively(_:_:)`](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md).

## Topics

### Constants
- [CFNetDiagnosticStatusValues.noErr](cfnetdiagnosticstatusvalues/noerr.md)
  No error occurred but there is no status.
- [CFNetDiagnosticStatusValues.err](cfnetdiagnosticstatusvalues/err.md)
  An error occurred that prevented the call from completing.
- [CFNetDiagnosticStatusValues.connectionUp](cfnetdiagnosticstatusvalues/connectionup.md)
  The connection appears to be working.
- [CFNetDiagnosticStatusValues.connectionIndeterminate](cfnetdiagnosticstatusvalues/connectionindeterminate.md)
  The status of the connection is not known.
- [CFNetDiagnosticStatusValues.connectionDown](cfnetdiagnosticstatusvalues/connectiondown.md)
  The connection does not appear to be working.
### Initializers
- [init?(rawValue: Int32)](cfnetdiagnosticstatusvalues/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CFNetDiagnostic](cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithstreams(_:_:_:).md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithurl(_:_:).md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](cfnetdiagnosticdiagnoseprobleminteractively(_:).md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](cfnetdiagnosticsetname(_:_:).md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues)*