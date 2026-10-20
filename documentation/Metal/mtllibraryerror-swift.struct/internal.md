# internal

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

The action caused an internal error.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var `internal`: MTLLibraryError.Code { get }
```

## See Also

### Errors
- [static var unsupported: MTLLibraryError.Code](./unsupported.md)
  Metal couldn’t support the requested action.
- [static var compileFailure: MTLLibraryError.Code](./compilefailure.md)
  The library or function failed to compile.
- [static var compileWarning: MTLLibraryError.Code](./compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [static var fileNotFound: MTLLibraryError.Code](./filenotfound.md)
  Metal couldn’t find the Metal source file.
- [static var functionNotFound: MTLLibraryError.Code](./functionnotfound.md)
  Metal couldn’t find the specified Metal function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/internal)*