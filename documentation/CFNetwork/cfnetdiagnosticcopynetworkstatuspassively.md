# CFNetDiagnosticCopyNetworkStatusPassively(_:_:)

**Framework**: CFNetwork  
**Kind**: func

Gets a network status value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus
```

#### Return Value

A network status value.

#### Discussion

This function returns a status value that can be used to display basic information about the connection, and optionally gets a localized string containing a description of the current network status.

This function is guaranteed not to generate network activity.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `details`: CFNetDiagnosticRef, created by   or  , for which the Network Diagnostics status is to be obtained.
- `description`: If not  , upon return contains a localized string containing a description of the current network status. Ownership follows the  .

## See Also

- [class CFNetDiagnostic](cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithstreams(_:_:_:).md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithurl(_:_:).md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](cfnetdiagnosticdiagnoseprobleminteractively(_:).md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](cfnetdiagnosticsetname(_:_:).md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcopynetworkstatuspassively(_:_:))*