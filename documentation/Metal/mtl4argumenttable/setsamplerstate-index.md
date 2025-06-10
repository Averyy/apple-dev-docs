# setSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a sampler state to a sampler state binding slot.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setSamplerState(_ resourceID: MTLResourceID, index bindingIndex: Int)
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

## Parameters

- `resourceID`: The   of the   instance to bind.
- `bindingIndex`: A valid binding index in the sampler binding range.   It is an error for this value to match or exceed the value of property    on the descriptor   from which you created this argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttable/setsamplerstate(_:index:))*