# fence

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An optional fence that this frame interpolator waits for and updates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var fence: (any MTLFence)? { get set }
```

#### Discussion

Use this property for synchronizing access to untracked resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/fence)*