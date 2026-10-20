# resourceAlias

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

Flushes caches to ensure that aliased virtual addresses are memory consistent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var resourceAlias: MTL4VisibilityOptions { get }
```

```c
MTL4VisibilityOptionResourceAlias
```

#### Discussion

On some systems this may be the GPU+CPU (system) memory coherence point and on other systems it may be the GPU (device) memory coherence point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4visibilityoptions/resourcealias)*