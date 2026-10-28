# MTLNewLibraryCompletionHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A completion handler signature a method calls when it finishes creating a Metal library.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLNewLibraryCompletionHandler = ((any MTLLibrary)?, (any Error)?) -> Void
```

```c
typedef void (^)(id<MTLLibrary>, NSError *) MTLNewLibraryCompletionHandler;
```

## Discussion

The framework reports compiler warnings to the console. The `error` parameter doesn’t report warnings because it’s `nil` when there aren’t any compiler errors.

## Parameters

- `library`: An [`MTLLibrary`](./mtllibrary.md) instance if the method successfully compiles the library without any errors; otherwise `nil`.
- `error`: An error instance if the compiler generates any errors; otherwise `nil`.

## See Also

### Creating shader libraries
- [func makeDefaultLibrary() -> (any MTLLibrary)?](./mtldevice/makedefaultlibrary%28%29.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [func makeDefaultLibrary(bundle: Bundle) throws -> any MTLLibrary](./mtldevice/makedefaultlibrary%28bundle%29.md)
  Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [func makeLibrary(URL: URL) throws -> any MTLLibrary](./mtldevice/makelibrary%28url%29.md)
  Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [func makeLibrary(source: String, options: MTLCompileOptions?) throws -> any MTLLibrary](./mtldevice/makelibrary%28source,options%29.md)
  Synchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](./mtldevice/makelibrary%28source,options,completionhandler%29.md)
  Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor) throws -> any MTLLibrary](./mtldevice/makelibrary%28stitcheddescriptor%29.md)
  Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](./mtldevice/makelibrary%28stitcheddescriptor,completionhandler%29.md)
  Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(data: DispatchData) throws -> any MTLLibrary](./mtldevice/makelibrary%28data%29-7khmh.md)
  Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [func makeLibrary(data: dispatch_data_t) throws -> any MTLLibrary](./mtldevice/makelibrary%28data%29.md)
  Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [func makeLibrary(filepath: String) throws -> any MTLLibrary](./mtldevice/makelibrary%28filepath%29.md)
  Creates a Metal library instance that contains the functions in the Metal library file at a file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewlibrarycompletionhandler)*