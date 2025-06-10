# shouldResetHistory

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A Boolean property indicating whether to reset history.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var shouldResetHistory: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to invalidate history, for example when there is a scene cut in your game.

When you set this property to [`false`](https://developer.apple.com/documentation/swift/false), you are responsible for ensuring the property [`prevColorTexture`](mtlfxframeinterpolatorbase/prevcolortexture.md) contains frame data corresponding to that in [`colorTexture`](mtlfxframeinterpolatorbase/colortexture.md) during your previous call to [`encode(to:)`](mtlfxframeinterpolator/encode(to:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/shouldresethistory)*