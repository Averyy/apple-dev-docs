# setAddress(_:attributeStride:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a GPU address to a buffer binding slot, providing a dynamic vertex stride.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setAddress(_ gpuAddress: MTLGPUAddress, attributeStride stride: Int, index bindingIndex: Int)
```

#### Discussion

This method requires that the value of property [`supportAttributeStrides`](mtl4argumenttabledescriptor/supportattributestrides.md) on the descriptor from which you created this argument table is true.

## Parameters

- `gpuAddress`: The GPU address of a   to set.
- `stride`: The stride between attributes in the buffer.
- `bindingIndex`: A valid binding index in the buffer binding range.   It is an error for this value to match or exceed the value of property    on the descriptor   from which you created this argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttable/setaddress(_:attributestride:index:))*