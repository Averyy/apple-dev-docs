# reset

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A Boolean that indicates whether the temporal scaler discards historical data from previous frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var reset: Bool { get set }
```

#### Discussion

Set to [`true`](https://developer.apple.com/documentation/swift/true) when the next frame your app encodes has no relevance to the previous frames, such as when changing scenes or perspectives.

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer)](mtlfxtemporalscaler/encode(commandbuffer:).md)
  Adds the temporal scaling command to a render pass’s command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/reset)*