# supportsRenderDynamicLibraries

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var supportsRenderDynamicLibraries: Bool { get }
```

## See Also

- [var supportsDynamicLibraries: Bool](mtldevice/supportsdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.
- [func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary](mtldevice/makedynamiclibrary(library:).md)
  Creates a Metal dynamic library instance from a Metal library instance.
- [func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary](mtldevice/makedynamiclibrary(url:).md)
  Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.
- [MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.
- [let MTLDynamicLibraryDomain: String](mtldynamiclibrarydomain.md)
  The domain for Metal dynamic library errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsrenderdynamiclibraries)*