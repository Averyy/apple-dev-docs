# makeLibrary(stitchedDescriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Synchronously creates a Metal library from the function stitching graphs in a descriptor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func makeLibrary(stitchedDescriptor descriptor: MTLStitchedLibraryDescriptor) throws -> any MTLLibrary
```

#### Return Value

A new [`MTLLibrary`](mtllibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `descriptor`: An   instance.

## See Also

- [func makeDefaultLibrary() -> (any MTLLibrary)?](mtldevice/makedefaultlibrary.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [func makeDefaultLibrary(bundle: Bundle) throws -> any MTLLibrary](mtldevice/makedefaultlibrary(bundle:).md)
  Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [func makeLibrary(URL: URL) throws -> any MTLLibrary](mtldevice/makelibrary(url:).md)
  Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [func makeLibrary(source: String, options: MTLCompileOptions?) throws -> any MTLLibrary](mtldevice/makelibrary(source:options:).md)
  Synchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](mtldevice/makelibrary(source:options:completionhandler:).md)
  Asynchronously creates a Metal library instance by compiling the functions in a source string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makelibrary(stitcheddescriptor:))*