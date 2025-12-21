# setAddress(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a GPU address to a buffer binding slot.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setAddress(_ gpuAddress: MTLGPUAddress, index bindingIndex: Int)
```

## Parameters

- `gpuAddress`: The GPU address of a   to set.
- `bindingIndex`: A valid binding index in the buffer binding range.   It is an error for this value to match or exceed the value of property    on the descriptor   from which you created this argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttable/setaddress(_:index:))*