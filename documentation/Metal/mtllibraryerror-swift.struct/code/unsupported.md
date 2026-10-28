# MTLLibraryError.Code.unsupported

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Metal couldn’t support the requested action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case unsupported
```

```c
MTLLibraryErrorUnsupported
```

## Discussion

For example, the requested library file has improper formatting, or the requested library is not accessible.

## See Also

### Errors
- [MTLLibraryError.Code.internal](./internal.md)
  The action caused an internal error.
- [MTLLibraryError.Code.compileFailure](./compilefailure.md)
  The library or function failed to compile.
- [MTLLibraryError.Code.compileWarning](./compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [MTLLibraryError.Code.fileNotFound](./filenotfound.md)
  Metal couldn’t find the Metal source file.
- [MTLLibraryError.Code.functionNotFound](./functionnotfound.md)
  Metal couldn’t find the specified Metal function.
- [MTLLibraryError.Code.internal](./internal.md)
  The action caused an internal error.
- [MTLLibraryError.Code.compileFailure](./compilefailure.md)
  The library or function failed to compile.
- [MTLLibraryError.Code.compileWarning](./compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [MTLLibraryError.Code.fileNotFound](./filenotfound.md)
  Metal couldn’t find the Metal source file.
- [MTLLibraryError.Code.functionNotFound](./functionnotfound.md)
  Metal couldn’t find the specified Metal function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/code/unsupported)*