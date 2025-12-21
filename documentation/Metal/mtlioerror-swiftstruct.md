# MTLIOError

**Framework**: Metal  
**Kind**: struct

The categories of errors for creating an input/output file handle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLIOError
```

## Topics

### Error codes
- [static var urlInvalid: MTLIOError.Code](mtlioerror-swift.struct/urlinvalid.md)
  An error that represents a problem with a file URL.
- [static var `internal`: MTLIOError.Code](mtlioerror-swift.struct/internal.md)
  An error that represents a problem internal to the Metal framework.
- [MTLIOError.Code](mtlioerror-swift.struct/code.md)
  The error codes for creating an input/output file handle.
### Error domain
- [static var errorDomain: String](mtlioerror-swift.struct/errordomain.md)
  The current error domain for input/output command queues.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MTLTensorError](mtltensorerror-swift.struct.md)
- [struct MTLBinaryArchiveError](mtlbinaryarchiveerror-swift.struct.md)
  An error that occurred when creating a binary shader archive.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [struct MTLComponentTransform](mtlcomponenttransform.md)
- [struct MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md)
  The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [struct MTLDynamicLibraryError](mtldynamiclibraryerror-swift.struct.md)
  Errors when compiling dynamic libraries.
- [struct MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [struct MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [struct NSDeviceCertification](nsdevicecertification.md)
- [struct NSProcessPerformanceProfile](nsprocessperformanceprofile.md)
  A value describing the device’s performance profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlioerror-swift.struct)*