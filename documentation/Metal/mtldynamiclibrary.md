# MTLDynamicLibrary

**Framework**: Metal  
**Kind**: protocol

A dynamically linkable representation of compiled shader code for a specific Metal device object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLDynamicLibrary : NSObjectProtocol, Sendable
```

## Topics

### Identifying the Library
- [var device: any MTLDevice](mtldynamiclibrary/device.md)
  The Metal device object that created the dynamic library.
- [var installName: String](mtldynamiclibrary/installname.md)
  A file path for this dynamic library.
- [var label: String?](mtldynamiclibrary/label.md)
  A string that identifies the library.
### Saving a Dynamic Library to a File
- [func serialize(to: URL) throws](mtldynamiclibrary/serialize(to:).md)
  Writes the contents of the dynamic library to a file.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLLibrary](mtllibrary.md)
  A collection of Metal shader functions.
- [protocol MTLBinaryArchive](mtlbinaryarchive.md)
  A container for pipeline state descriptors and their associated compiled shader code.
- [class MTLCompileOptions](mtlcompileoptions.md)
  Compilation settings for a Metal shader library.
- [enum MTLLibraryType](mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibrary)*