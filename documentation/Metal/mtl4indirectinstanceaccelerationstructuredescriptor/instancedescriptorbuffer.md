# instanceDescriptorBuffer

**Framework**: Metal  
**Kind**: property

Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var instanceDescriptorBuffer: MTL4BufferRange { get set }
```

#### Discussion

This buffer conceptually represents an array of instance data. The specific format for the structs that comprise each entry depends on the value of the  [`instanceDescriptorType`](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype.md) property.

You are responsible for ensuring the buffer address the range contains is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer)*