# reset

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean that indicates whether the temporal scaler discards historical data from previous frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var reset: Bool { get set }
```

```objc
@property (nonatomic) BOOL reset;
```

## Discussion

Set to [`true`](../../Swift/true.md) when the next frame your app encodes has no relevance to the previous frames, such as when changing scenes or perspectives.

## See Also

### Encoding a temporal scaling effect
- [func encode(commandBuffer: any MTLCommandBuffer)](../mtlfxtemporalscaler/encode%28commandbuffer%29.md)
  Adds the temporal scaling command to a render pass’s command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/reset)*