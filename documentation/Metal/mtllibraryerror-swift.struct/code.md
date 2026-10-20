# MTLLibraryError.Code

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Error codes for Metal library errors.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum MTLLibraryError : NSUInteger;
```

## Topics

### Errors
- [MTLLibraryError.Code.unsupported](./code/unsupported.md)
  Metal couldn’t support the requested action.
- [MTLLibraryError.Code.internal](./code/internal.md)
  The action caused an internal error.
- [MTLLibraryError.Code.compileFailure](./code/compilefailure.md)
  The library or function failed to compile.
- [MTLLibraryError.Code.compileWarning](./code/compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [MTLLibraryError.Code.fileNotFound](./code/filenotfound.md)
  Metal couldn’t find the Metal source file.
- [MTLLibraryError.Code.functionNotFound](./code/functionnotfound.md)
  Metal couldn’t find the specified Metal function.
- [MTLLibraryError.Code.unsupported](./code/unsupported.md)
  Metal couldn’t support the requested action.
- [MTLLibraryError.Code.internal](./code/internal.md)
  The action caused an internal error.
- [MTLLibraryError.Code.compileFailure](./code/compilefailure.md)
  The library or function failed to compile.
- [MTLLibraryError.Code.compileWarning](./code/compilewarning.md)
  The library or function compiled successfully but generated warnings.
- [MTLLibraryError.Code.fileNotFound](./code/filenotfound.md)
  Metal couldn’t find the Metal source file.
- [MTLLibraryError.Code.functionNotFound](./code/functionnotfound.md)
  Metal couldn’t find the specified Metal function.
### Initializers
- [init?(rawValue: UInt)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct MTLLibraryError](../mtllibraryerror-swift.struct.md)
  Metal errors related to libraries.
- [let MTLLibraryErrorDomain: String](../mtllibraryerrordomain.md)
  The error domain for Metal libraries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/code)*