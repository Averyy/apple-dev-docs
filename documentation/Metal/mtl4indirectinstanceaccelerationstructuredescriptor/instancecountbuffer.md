# instanceCountBuffer

**Framework**: Metal  
**Kind**: property

Provides a reference to a buffer containing the number of instances in the instance descriptor buffer, formatted as a 32-bit unsigned integer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var instanceCountBuffer: MTL4BufferRange { get set }
```

#### Discussion

You are responsible for ensuring that the final number of instances at build time, which you provide indirectly via this buffer reference , is less than or equal to the value of property [`maxInstanceCount`](mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer)*