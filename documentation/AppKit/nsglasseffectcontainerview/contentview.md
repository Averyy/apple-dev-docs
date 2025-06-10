# contentView

**Framework**: AppKit  
**Kind**: property

NSGlassViews that are descendents of an NSGlassContainerView’s contentView will 1) have their z-order elevated above that of the contentView 2) if the NSGlassViews are sufficiently similar, they will merge together in close proximity 3) can process similar NSGlassViews as a batch, to improve performance.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview/contentview)*