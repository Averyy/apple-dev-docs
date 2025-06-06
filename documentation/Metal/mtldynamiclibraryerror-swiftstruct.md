# MTLDynamicLibraryError

**Framework**: Metal  
**Kind**: struct

Errors when compiling dynamic libraries.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLDynamicLibraryError
```

## Topics

### Error Codes
- [static var none: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/none.md)
  An error code that represents the absence of any problems.
- [static var invalidFile: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/invalidfile.md)
  An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [static var compilationFailure: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/compilationfailure.md)
  An error code that indicates Metal couldn’t compile a dynamic library.
- [static var unresolvedInstallName: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/unresolvedinstallname.md)
  An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [static var dependencyLoadFailure: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/dependencyloadfailure.md)
  An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [static var unsupported: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/unsupported.md)
  An error code that indicates the GPU device doesn’t support dynamic libraries.
- [MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.
### Error Domain
- [static var errorDomain: String](mtldynamiclibraryerror-swift.struct/errordomain.md)
  The current dynamic library error domain.
- [let MTLDynamicLibraryDomain: String](mtldynamiclibrarydomain.md)
  The domain for Metal dynamic library errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLBinaryArchiveError](mtlbinaryarchiveerror-swift.struct.md)
  An error that occurred when creating a binary shader archive.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [struct MTLComponentTransform](mtlcomponenttransform.md)
- [struct MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md)
  The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [struct MTLIOError](mtlioerror-swift.struct.md)
  The categories of errors for creating an input/output file handle.
- [struct MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [struct MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [struct NSDeviceCertification](nsdevicecertification.md)
- [struct NSProcessPerformanceProfile](nsprocessperformanceprofile.md)
  A value describing the device’s performance profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibraryerror-swift.struct)*