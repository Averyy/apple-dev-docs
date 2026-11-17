# encode(commandBuffer:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the temporal scaling command to a render pass’s command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer;
```

## Parameters

- `commandBuffer`: The destination command buffer for a render pass.

## See Also

### Encoding a temporal scaling effect
- [var reset: Bool](../mtlfxtemporalscalerbase/reset.md)
  A Boolean that indicates whether the temporal scaler discards historical data from previous frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/encode(commandbuffer:))*