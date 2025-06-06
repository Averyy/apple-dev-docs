# CFNetDiagnosticCreateWithURL(_:_:)

**Framework**: CFNetwork  
**Kind**: func

Creates a CFNetDiagnosticRef from a CFURLRef.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetDiagnosticCreateWithURL(_ alloc: CFAllocator, _ url: CFURL) -> Unmanaged<CFNetDiagnostic>
```

#### Return Value

CFNetDiagnosticRef that you can pass to [`CFNetDiagnosticDiagnoseProblemInteractively(_:)`](cfnetdiagnosticdiagnoseprobleminteractively(_:).md) or [`CFNetDiagnosticCopyNetworkStatusPassively(_:_:)`](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md). Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function uses a URL to create a reference to an instance of a CFNetDiagnostic object. You can pass the reference to [`CFNetDiagnosticDiagnoseProblemInteractively(_:)`](cfnetdiagnosticdiagnoseprobleminteractively(_:).md) to open a Network Diagnostics window or to [`CFNetDiagnosticCopyNetworkStatusPassively(_:_:)`](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md) to get a description of the connection referenced by `readStream` and `writeStream`.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `url`: CFURLRef that refers to the failed connection.

## See Also

- [class CFNetDiagnostic](cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithstreams(_:_:_:).md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](cfnetdiagnosticdiagnoseprobleminteractively(_:).md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](cfnetdiagnosticsetname(_:_:).md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcreatewithurl(_:_:))*