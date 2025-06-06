# MTLBinaryArchiveError

**Framework**: Metal  
**Kind**: struct

An error that occurred when creating a binary shader archive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLBinaryArchiveError
```

## Topics

### Error Codes
- [static var none: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/none.md)
  An error code that represents the absence of any problems.
- [static var invalidFile: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [static var compilationFailure: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [static var unexpectedElement: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [static var internalError: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/internalerror.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/code.md)
  Error codes when creating binary archives of compiled shader code.
### Error Domain
- [static var errorDomain: String](mtlbinaryarchiveerror-swift.struct/errordomain.md)
  The current binary archive error domain.
- [let MTLBinaryArchiveDomain: String](mtlbinaryarchivedomain.md)
  The domain for Metal binary archive errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [struct MTLComponentTransform](mtlcomponenttransform.md)
- [struct MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md)
  The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [struct MTLDynamicLibraryError](mtldynamiclibraryerror-swift.struct.md)
  Errors when compiling dynamic libraries.
- [struct MTLIOError](mtlioerror-swift.struct.md)
  The categories of errors for creating an input/output file handle.
- [struct MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [struct MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [struct NSDeviceCertification](nsdevicecertification.md)
- [struct NSProcessPerformanceProfile](nsprocessperformanceprofile.md)
  A value describing the device’s performance profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct)*