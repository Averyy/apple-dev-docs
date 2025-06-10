# storageMode

**Framework**: Metal  
**Kind**: property

A value that configures the memory location and access permissions of tensors you create with this descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var storageMode: MTLStorageMode { get set }
```

#### Discussion

The default value of this property defaults to [`MTLStorageMode.shared`](mtlstoragemode/shared.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/storagemode)*