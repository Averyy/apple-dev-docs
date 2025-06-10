# setAddress(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a GPU address to a buffer binding slot.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setAddress(_ gpuAddress: UInt64, index bindingIndex: Int)
```

## Parameters

- `gpuAddress`: The GPU address of a   to set.
- `bindingIndex`: A valid binding index in the buffer binding range.   It is an error for this value to match or exceed the value of property    on the descriptor   from which you created this argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttable/setaddress(_:index:))*