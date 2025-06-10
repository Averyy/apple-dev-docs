# contentView

**Framework**: AppKit  
**Kind**: property

The view to be embedded in glass. Note that only the contentView of the NSGlassView is guaranteed to be placed inside the glass effect. Arbitrary subviews are not guaranteed any specific behavior regarding z-order against the content view or glass effect.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectview/contentview)*