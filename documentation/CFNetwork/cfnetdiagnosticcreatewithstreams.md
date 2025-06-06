# CFNetDiagnosticCreateWithStreams(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Creates a network diagnostic object from a pair of CFStreams.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetDiagnosticCreateWithStreams(_ alloc: CFAllocator?, _ readStream: CFReadStream?, _ writeStream: CFWriteStream?) -> Unmanaged<CFNetDiagnostic>
```

#### Discussion

This function uses references to a read steam and a write stream (or just a read stream or just a write stream) to create a reference to an instance of a CFNetDiagnostic object. You can pass the reference to [`CFNetDiagnosticDiagnoseProblemInteractively(_:)`](cfnetdiagnosticdiagnoseprobleminteractively(_:).md) to open a Network Diagnostics window or to [`CFNetDiagnosticCopyNetworkStatusPassively(_:_:)`](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md) to get a description of the connection referenced by `readStream` and `writeStream`.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same CFNetDiagnosticRef at the same time.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `readStream`: Reference to a read stream whose connection has failed, or   if you do not want the CFNetDiagnosticRef to have a read stream.
- `writeStream`: Reference to a write stream whose connection has failed, or   if you do not want the CFNetDiagnosticRef to have a write stream.

## See Also

- [class CFNetDiagnostic](cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithurl(_:_:).md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](cfnetdiagnosticdiagnoseprobleminteractively(_:).md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](cfnetdiagnosticsetname(_:_:).md)
  Overrides the displayed application name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcreatewithstreams(_:_:_:))*