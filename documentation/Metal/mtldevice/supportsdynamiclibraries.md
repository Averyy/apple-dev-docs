# supportsDynamicLibraries

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var supportsDynamicLibraries: Bool { get }
```

```objc
@property (readonly) BOOL supportsDynamicLibraries;
```

## See Also

### Creating dynamic shader libraries
- [var supportsRenderDynamicLibraries: Bool](./supportsrenderdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary](./makedynamiclibrary%28library%29.md)
  Creates a Metal dynamic library instance from a Metal library instance.
- [func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary](./makedynamiclibrary%28url%29.md)
  Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.
- [MTLDynamicLibraryError.Code](../mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.
- [let MTLDynamicLibraryDomain: String](../mtldynamiclibrarydomain.md)
  The domain for Metal dynamic library errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsdynamiclibraries)*