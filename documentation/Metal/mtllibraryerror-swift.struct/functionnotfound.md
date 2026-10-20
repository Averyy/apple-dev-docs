# functionNotFound

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

Metal couldn’t find the specified Metal function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var functionNotFound: MTLLibraryError.Code { get }
```

## See Also

### Errors
- [static var unsupported: MTLLibraryError.Code](./unsupported.md)
  Metal couldn’t support the requested action.
- [static var `internal`: MTLLibraryError.Code](./internal.md)
  The action caused an internal error.
- [static var compileFailure: MTLLibraryError.Code](./compilefailure.md)
  The library or function failed to compile.
- [static var compileWarning: MTLLibraryError.Code](./compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [static var fileNotFound: MTLLibraryError.Code](./filenotfound.md)
  Metal couldn’t find the Metal source file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/functionnotfound)*