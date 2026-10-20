# preloadedLibraries

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Provides an array of dynamic libraries the compiler loads when it builds the pipeline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var preloadedLibraries: [any MTLDynamicLibrary] { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSArray<id<MTLDynamicLibrary>> * preloadedLibraries;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor/preloadedlibraries)*