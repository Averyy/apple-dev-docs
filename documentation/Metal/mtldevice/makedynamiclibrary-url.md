# makeDynamicLibrary(url:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary
```

## Mentions

- [Compiling and Linking Metal Dynamic Libraries](compiling-and-linking-metal-dynamic-libraries.md)

#### Return Value

A new [`MTLDynamicLibrary`](mtldynamiclibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `url`: A URL to a Metal library file (ending in  ).

## See Also

- [var supportsDynamicLibraries: Bool](mtldevice/supportsdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.
- [var supportsRenderDynamicLibraries: Bool](mtldevice/supportsrenderdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary](mtldevice/makedynamiclibrary(library:).md)
  Creates a Metal dynamic library instance from a Metal library instance.
- [MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.
- [let MTLDynamicLibraryDomain: String](mtldynamiclibrarydomain.md)
  The domain for Metal dynamic library errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makedynamiclibrary(url:))*