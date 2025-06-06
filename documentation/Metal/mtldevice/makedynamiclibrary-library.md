# makeDynamicLibrary(library:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a Metal dynamic library instance from a Metal library instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary
```

#### Return Value

A new [`MTLDynamicLibrary`](mtldynamiclibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `library`: An   instance.

## See Also

- [var supportsDynamicLibraries: Bool](mtldevice/supportsdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.
- [var supportsRenderDynamicLibraries: Bool](mtldevice/supportsrenderdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary](mtldevice/makedynamiclibrary(url:).md)
  Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.
- [MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.
- [let MTLDynamicLibraryDomain: String](mtldynamiclibrarydomain.md)
  The domain for Metal dynamic library errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makedynamiclibrary(library:))*