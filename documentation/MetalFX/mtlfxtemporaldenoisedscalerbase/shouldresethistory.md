# shouldResetHistory

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A Boolean property indicating whether to reset history.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var shouldResetHistory: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to invalidate history, for example when there is a scene cut in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/shouldresethistory)*