# MTLLibraryOptimizationLevel

**Framework**: Metal  
**Kind**: enum

The optimization options for the Metal compiler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLLibraryOptimizationLevel
```

## Topics

### Optimization Options
- [MTLLibraryOptimizationLevel.default](mtllibraryoptimizationlevel/default.md)
  An optimization option for the Metal compiler that prioritizes runtime performance.
- [MTLLibraryOptimizationLevel.size](mtllibraryoptimizationlevel/size.md)
  An optimization option for the Metal compiler that prioritizes minimizing the size of its output binaries, which may also reduce compile time.
### Initializers
- [init?(rawValue: Int)](mtllibraryoptimizationlevel/init(rawvalue:).md)

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
- [enum MTLLibraryType](mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryoptimizationlevel)*