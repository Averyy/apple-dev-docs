# contentView

**Framework**: AppKit  
**Kind**: property

The view to embed in glass.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```

#### Discussion

> ❗ **Important**: `NSGlassEffectView` only guarantees the `contentView` will be placed inside the glass effect; arbitrary subviews aren’t guaranteed specific behavior with regard to z-order in relation to the content view or glass effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectview/contentview)*