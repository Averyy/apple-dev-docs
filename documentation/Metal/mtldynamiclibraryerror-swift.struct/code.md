# MTLDynamicLibraryError.Code

**Framework**: Metal  
**Kind**: enum

Error codes that Metal can generate when creating dynamic libraries.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
- [MTLDynamicLibraryError.Code.none](mtldynamiclibraryerror-swift.struct/code/none.md)
  An error code that represents the absence of any problems.
- [MTLDynamicLibraryError.Code.invalidFile](mtldynamiclibraryerror-swift.struct/code/invalidfile.md)
  An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [MTLDynamicLibraryError.Code.compilationFailure](mtldynamiclibraryerror-swift.struct/code/compilationfailure.md)
  An error code that indicates Metal couldn’t compile a dynamic library.
- [MTLDynamicLibraryError.Code.unresolvedInstallName](mtldynamiclibraryerror-swift.struct/code/unresolvedinstallname.md)
  An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [MTLDynamicLibraryError.Code.dependencyLoadFailure](mtldynamiclibraryerror-swift.struct/code/dependencyloadfailure.md)
  An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [MTLDynamicLibraryError.Code.unsupported](mtldynamiclibraryerror-swift.struct/code/unsupported.md)
  An error code that indicates the GPU device doesn’t support dynamic libraries.
- [MTLDynamicLibraryError.Code.none](mtldynamiclibraryerror-swift.struct/code/none.md)
  An error code that represents the absence of any problems.
- [MTLDynamicLibraryError.Code.invalidFile](mtldynamiclibraryerror-swift.struct/code/invalidfile.md)
  An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [MTLDynamicLibraryError.Code.compilationFailure](mtldynamiclibraryerror-swift.struct/code/compilationfailure.md)
  An error code that indicates Metal couldn’t compile a dynamic library.
- [MTLDynamicLibraryError.Code.unresolvedInstallName](mtldynamiclibraryerror-swift.struct/code/unresolvedinstallname.md)
  An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [MTLDynamicLibraryError.Code.dependencyLoadFailure](mtldynamiclibraryerror-swift.struct/code/dependencyloadfailure.md)
  An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [MTLDynamicLibraryError.Code.unsupported](mtldynamiclibraryerror-swift.struct/code/unsupported.md)
  An error code that indicates the GPU device doesn’t support dynamic libraries.
### Initializers
- [init?(rawValue: UInt)](mtldynamiclibraryerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibraryerror-swift.struct/code)*