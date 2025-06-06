# compileFailure

**Framework**: Metal  
**Kind**: property

The library or function failed to compile.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static var compileFailure: MTLLibraryError.Code { get }
```

## See Also

- [static var unsupported: MTLLibraryError.Code](mtllibraryerror-swift.struct/unsupported.md)
  Metal couldn’t support the requested action.
- [static var `internal`: MTLLibraryError.Code](mtllibraryerror-swift.struct/internal.md)
  The action caused an internal error.
- [static var compileWarning: MTLLibraryError.Code](mtllibraryerror-swift.struct/compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [static var fileNotFound: MTLLibraryError.Code](mtllibraryerror-swift.struct/filenotfound.md)
  Metal couldn’t find the Metal source file.
- [static var functionNotFound: MTLLibraryError.Code](mtllibraryerror-swift.struct/functionnotfound.md)
  Metal couldn’t find the specified Metal function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/compilefailure)*