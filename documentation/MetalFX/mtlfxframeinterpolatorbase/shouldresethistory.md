# shouldResetHistory

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean property indicating whether to reset history.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var shouldResetHistory: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldResetHistory;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to invalidate history, for example when there is a scene cut in your game.

When you set this property to [`false`](../../Swift/false.md), you are responsible for ensuring the property [`prevColorTexture`](./prevcolortexture.md) contains frame data corresponding to that in [`colorTexture`](./colortexture.md) during your previous call to [`encode(commandBuffer:)`](../mtlfxframeinterpolator/encode%28commandbuffer%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/shouldresethistory)*