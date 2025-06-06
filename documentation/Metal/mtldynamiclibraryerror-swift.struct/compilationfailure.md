# compilationFailure

**Framework**: Metal  
**Kind**: property

An error code that indicates Metal couldn’t compile a dynamic library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var compilationFailure: MTLDynamicLibraryError.Code { get }
```

## See Also

- [static var none: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/none.md)
  An error code that represents the absence of any problems.
- [static var invalidFile: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/invalidfile.md)
  An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [static var unresolvedInstallName: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/unresolvedinstallname.md)
  An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [static var dependencyLoadFailure: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/dependencyloadfailure.md)
  An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [static var unsupported: MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/unsupported.md)
  An error code that indicates the GPU device doesn’t support dynamic libraries.
- [MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibraryerror-swift.struct/compilationfailure)*