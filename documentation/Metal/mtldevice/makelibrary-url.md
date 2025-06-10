# makeLibrary(URL:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a Metal library instance that contains the functions in the Metal library file at a URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeLibrary(URL url: URL) throws -> any MTLLibrary
```

## Mentions

- [Building a Shader Library by Precompiling Source Files](building-a-shader-library-by-precompiling-source-files.md)

#### Return Value

A new [`MTLLibrary`](mtllibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `url`: A URL to a Metal library file (ending in  ).

## See Also

- [func makeDefaultLibrary() -> (any MTLLibrary)?](mtldevice/makedefaultlibrary.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [func makeDefaultLibrary(bundle: Bundle) throws -> any MTLLibrary](mtldevice/makedefaultlibrary(bundle:).md)
  Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [func makeLibrary(source: String, options: MTLCompileOptions?) throws -> any MTLLibrary](mtldevice/makelibrary(source:options:).md)
  Synchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](mtldevice/makelibrary(source:options:completionhandler:).md)
  Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor) throws -> any MTLLibrary](mtldevice/makelibrary(stitcheddescriptor:).md)
  Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](mtldevice/makelibrary(stitcheddescriptor:completionhandler:).md)
  Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(data: DispatchData) throws -> any MTLLibrary](mtldevice/makelibrary(data:)-7khmh.md)
  Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [func makeLibrary(data: dispatch_data_t) throws -> any MTLLibrary](mtldevice/makelibrary(data:).md)
  Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [typealias MTLNewLibraryCompletionHandler](mtlnewlibrarycompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a Metal library.
- [func makeLibrary(filepath: String) throws -> any MTLLibrary](mtldevice/makelibrary(filepath:).md)
  Creates a Metal library instance that contains the functions in the Metal library file at a file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makelibrary(url:))*