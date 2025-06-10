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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/shouldresethistory)*