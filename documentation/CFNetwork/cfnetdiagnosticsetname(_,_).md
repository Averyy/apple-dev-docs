# CFNetDiagnosticSetName(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Overrides the displayed application name.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func CFNetDiagnosticSetName(_ details: CFNetDiagnostic, _ name: CFString)
```

```c
extern void CFNetDiagnosticSetName(CFNetDiagnosticRef details, CFStringRef name);
```

#### Discussion

Frameworks requiring that an application name be displayed to the user derive the application name from the bundle identifier of the currently running application, in that application’s localization. If you want to override the derived application name, use this function to set the name that is displayed.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `details`: The network diagnostics object for which the application name is to be set.
- `name`: Name that is to be set.

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
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](./cfnetdiagnosticdiagnoseprobleminteractively%28_%29.md)
  Opens a Network Diagnostics window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticsetname(_:_:))*