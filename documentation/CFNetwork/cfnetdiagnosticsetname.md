# CFNetDiagnosticSetName(_:_:)

**Framework**: CFNetwork  
**Kind**: func

Overrides the displayed application name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetDiagnosticSetName(_ details: CFNetDiagnostic, _ name: CFString)
```

#### Discussion

Frameworks requiring that an application name be displayed to the user derive the application name from the bundle identifier of the currently running application, in that application’s localization. If you want to override the derived application name, use this function to set the name that is displayed.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `details`: The network diagnostics object for which the application name is to be set.
- `name`: Name that is to be set.

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
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](cfnetdiagnosticdiagnoseprobleminteractively(_:).md)
  Opens a Network Diagnostics window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticsetname(_:_:))*