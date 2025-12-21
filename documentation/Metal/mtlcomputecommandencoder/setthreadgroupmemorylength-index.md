# setThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a block of threadgroup memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, index: Int)
```

#### Discussion

> ❗ **Important**:  The sum of all threadgroup memory allocations (whether made using this method or directly in the shader) can’t exceed the device limits for threadgroup memory. Check threadgroup memory limits with the [`staticThreadgroupMemoryLength`](mtlcomputepipelinestate/staticthreadgroupmemorylength.md) property.

The `threadgroup` memory space allows for sharing data between multiple threads in a threadgroup, which can be faster than using `device` memory in your kernels. Before using any threadgroup memory, call this method to configure the threadgroup memory argument table. Kernels accessing their arguments from threadgroup memory have the `[[threadgroup]]` attribute.

To learn more about using the threadgroup address space, see the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/metal-shading-language-specification.pdf#//apple_ref/doc/uid/TP40014364-CH4-SW5) section 4.4.

## Parameters

- `length`: The size of the threadgroup memory, in bytes, which needs to be a multiple of   bytes.
- `index`: The index in the threadgroup memory argument table using this allocation.

## See Also

- [func setImageblockWidth(Int, height: Int)](mtlcomputecommandencoder/setimageblockwidth(_:height:).md)
  Sets the size, in pixels, of imageblock data in tile memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setthreadgroupmemorylength(_:index:))*