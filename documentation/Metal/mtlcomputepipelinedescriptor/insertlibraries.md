# insertLibraries

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The dynamic libraries that contain precompiled shader functions you want to link.

**Availability**:
- iOS 14.0+ - Deprecated in 15.0
- iPadOS 14.0+ - Deprecated in 15.0
- Mac Catalyst 14.0+ - Deprecated in 15.0
- macOS 11.0+ - Deprecated in 12.0
- tvOS 14.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`preloadedLibraries`](./preloadedlibraries.md) property instead.

## Declaration

```swift
var insertLibraries: [any MTLDynamicLibrary]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<id<MTLDynamicLibrary>> * insertLibraries;
```

## See Also

### Loading dynamic libraries to link at runtime
- [var preloadedLibraries: [any MTLDynamicLibrary]](./preloadedlibraries.md)
  The dynamic libraries that contain precompiled shader functions you want to link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/insertlibraries)*