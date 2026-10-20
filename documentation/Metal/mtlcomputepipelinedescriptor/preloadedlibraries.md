# preloadedLibraries

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The dynamic libraries that contain precompiled shader functions you want to link.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var preloadedLibraries: [any MTLDynamicLibrary] { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSArray<id<MTLDynamicLibrary>> * preloadedLibraries;
```

## See Also

### Loading dynamic libraries to link at runtime
- [var insertLibraries: [any MTLDynamicLibrary]?](./insertlibraries.md)
  The dynamic libraries that contain precompiled shader functions you want to link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/preloadedlibraries)*