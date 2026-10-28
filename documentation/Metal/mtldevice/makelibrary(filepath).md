# makeLibrary(filepath:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a Metal library instance that contains the functions in the Metal library file at a file path.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`makeLibrary(URL:)`](./makelibrary%28url%29.md) instead.

## Declaration

```swift
func makeLibrary(filepath: String) throws -> any MTLLibrary
```

```objc
- (id<MTLLibrary>) newLibraryWithFile:(NSString *) filepath error:(NSError **) error;
```

## Return Value

A new [`MTLLibrary`](../mtllibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `filepath`: A string of the absolute file path to a Metal library file (ending in `.metallib`).

## See Also

### Creating shader libraries
- [func makeDefaultLibrary() -> (any MTLLibrary)?](./makedefaultlibrary%28%29.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [func makeDefaultLibrary(bundle: Bundle) throws -> any MTLLibrary](./makedefaultlibrary%28bundle%29.md)
  Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [func makeLibrary(URL: URL) throws -> any MTLLibrary](./makelibrary%28url%29.md)
  Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [func makeLibrary(source: String, options: MTLCompileOptions?) throws -> any MTLLibrary](./makelibrary%28source,options%29.md)
  Synchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](./makelibrary%28source,options,completionhandler%29.md)
  Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor) throws -> any MTLLibrary](./makelibrary%28stitcheddescriptor%29.md)
  Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](./makelibrary%28stitcheddescriptor,completionhandler%29.md)
  Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(data: DispatchData) throws -> any MTLLibrary](./makelibrary%28data%29-7khmh.md)
  Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [func makeLibrary(data: dispatch_data_t) throws -> any MTLLibrary](./makelibrary%28data%29.md)
  Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [typealias MTLNewLibraryCompletionHandler](../mtlnewlibrarycompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makelibrary(filepath:))*