# CFNetDiagnosticStatusValues

**Framework**: CFNetwork  
**Kind**: enum  
**Role**: Enumeration

Constants for diagnostic status values.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
enum CFNetDiagnosticStatusValues
```

```c
enum CFNetDiagnosticStatusValues : int;
```

#### Overview

Diagnostic status values are returned by [`CFNetDiagnosticDiagnoseProblemInteractively(_:)`](./cfnetdiagnosticdiagnoseprobleminteractively%28_%29.md) and [`CFNetDiagnosticCopyNetworkStatusPassively(_:_:)`](./cfnetdiagnosticcopynetworkstatuspassively%28_,_%29.md).

## Topics

### Constants
- [CFNetDiagnosticStatusValues.noErr](./cfnetdiagnosticstatusvalues/noerr.md)
  No error occurred but there is no status.
- [CFNetDiagnosticStatusValues.err](./cfnetdiagnosticstatusvalues/err.md)
  An error occurred that prevented the call from completing.
- [CFNetDiagnosticStatusValues.connectionUp](./cfnetdiagnosticstatusvalues/connectionup.md)
  The connection appears to be working.
- [CFNetDiagnosticStatusValues.connectionIndeterminate](./cfnetdiagnosticstatusvalues/connectionindeterminate.md)
  The status of the connection is not known.
- [CFNetDiagnosticStatusValues.connectionDown](./cfnetdiagnosticstatusvalues/connectiondown.md)
  The connection does not appear to be working.
### Initializers
- [init?(rawValue: Int32)](./cfnetdiagnosticstatusvalues/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Network Diagnostics
- [class CFNetDiagnostic](./cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](./cfnetdiagnosticcopynetworkstatuspassively%28_,_%29.md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](./cfnetdiagnosticcreatewithstreams%28_,_,_%29.md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](./cfnetdiagnosticcreatewithurl%28_,_%29.md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](./cfnetdiagnosticdiagnoseprobleminteractively%28_%29.md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](./cfnetdiagnosticsetname%28_,_%29.md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues)*