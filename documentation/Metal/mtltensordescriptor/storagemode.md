# storageMode

**Framework**: Metal  
**Kind**: property

A value that configures the memory location and access permissions of tensors you create with this descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var storageMode: MTLStorageMode { get set }
```

#### Discussion

The default value of this property defaults to [`MTLStorageMode.shared`](mtlstoragemode/shared.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/storagemode)*