# fence

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An optional fence that this denoiser scaler waits for and updates.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fence: (any MTLFence)? { get set }
```

#### Discussion

Use this property for synchronizing access to untracked resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/fence)*