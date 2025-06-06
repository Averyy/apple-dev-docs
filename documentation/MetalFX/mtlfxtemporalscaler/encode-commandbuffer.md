# encode(commandBuffer:)

**Framework**: MetalFX  
**Kind**: method  
**Required**: Yes

Adds the temporal scaling command to a render pass’s command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer)
```

## Parameters

- `commandBuffer`: The destination command buffer for a render pass.

## See Also

- [var reset: Bool](mtlfxtemporalscaler/reset.md)
  A Boolean that indicates whether the temporal scaler discards historical data from previous frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/encode(commandbuffer:))*