# MTLLibraryType

**Framework**: Metal  
**Kind**: enum

A set of options for Metal library types.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLLibraryType
```

## Topics

### Library options
- [MTLLibraryType.executable](mtllibrarytype/executable.md)
  A library that can create pipeline state objects.
- [MTLLibraryType.dynamic](mtllibrarytype/dynamic.md)
  A library that you can dynamically link to from other libraries.
### Initializers
- [init?(rawValue: Int)](mtllibrarytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLLibrary](mtllibrary.md)
  A collection of Metal shader functions.
- [protocol MTLDynamicLibrary](mtldynamiclibrary.md)
  A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [protocol MTLBinaryArchive](mtlbinaryarchive.md)
  A container for pipeline state descriptors and their associated compiled shader code.
- [class MTLCompileOptions](mtlcompileoptions.md)
  Compilation settings for a Metal shader library.
- [enum MTLLanguageVersion](mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrarytype)*