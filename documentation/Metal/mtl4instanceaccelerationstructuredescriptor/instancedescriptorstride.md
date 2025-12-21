# instanceDescriptorStride

**Framework**: Metal  
**Kind**: property

Sets the stride, in bytes, between instance descriptors the instance descriptor buffer references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var instanceDescriptorStride: Int { get set }
```

#### Discussion

You are responsible for ensuring this stride is at least the size of the structure type corresponding to the instance descriptor type and a multiple of 4 bytes.

Defaults to `0`, indicating the instance descriptors are tightly packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancedescriptorstride)*