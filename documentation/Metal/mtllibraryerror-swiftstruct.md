# MTLLibraryError

**Framework**: Metal  
**Kind**: struct

Metal errors related to libraries.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct MTLLibraryError
```

## Topics

### Errors
- [static var unsupported: MTLLibraryError.Code](mtllibraryerror-swift.struct/unsupported.md)
  Metal couldn’t support the requested action.
- [static var `internal`: MTLLibraryError.Code](mtllibraryerror-swift.struct/internal.md)
  The action caused an internal error.
- [static var compileFailure: MTLLibraryError.Code](mtllibraryerror-swift.struct/compilefailure.md)
  The library or function failed to compile.
- [static var compileWarning: MTLLibraryError.Code](mtllibraryerror-swift.struct/compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [static var fileNotFound: MTLLibraryError.Code](mtllibraryerror-swift.struct/filenotfound.md)
  Metal couldn’t find the Metal source file.
- [static var functionNotFound: MTLLibraryError.Code](mtllibraryerror-swift.struct/functionnotfound.md)
  Metal couldn’t find the specified Metal function.
### Error Domain
- [static var errorDomain: String](mtllibraryerror-swift.struct/errordomain.md)
  The error domain used by Metal when returning library or function creation errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MTLLibraryError.Code](mtllibraryerror-swift.struct/code.md)
  Error codes for Metal library errors.
- [let MTLLibraryErrorDomain: String](mtllibraryerrordomain.md)
  The error domain for Metal libraries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct)*