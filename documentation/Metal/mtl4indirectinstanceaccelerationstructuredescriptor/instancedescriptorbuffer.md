# instanceDescriptorBuffer

**Framework**: Metal  
**Kind**: property

Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var instanceDescriptorBuffer: MTL4BufferRange { get set }
```

#### Discussion

This buffer conceptually represents an array of instance data. The specific format for the structs that comprise each entry depends on the value of the  [`instanceDescriptorType`](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype.md) property.

You are responsible for ensuring the buffer address the range contains is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer)*