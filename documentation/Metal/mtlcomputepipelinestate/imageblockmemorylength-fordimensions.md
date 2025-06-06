# imageblockMemoryLength(forDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the length of reserved memory for an imageblock of a given size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func imageblockMemoryLength(forDimensions imageblockDimensions: MTLSize) -> Int
```

#### Return Value

The length, in bytes, occupied by the image block in memory.

## Parameters

- `imageblockDimensions`: An   instance that represents the dimensions of an imageblock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/imageblockmemorylength(fordimensions:))*