# spacing

**Framework**: AppKit  
**Kind**: property

Controls the proximity at which descendent NSGlassViews will begin merging with eachother, if they are otherwise eligable. The default value (0) is sufficient for batch processing the effects of eligable NSGlassViews, while avoiding distortion and merging effects for views in close proximity.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var spacing: CGFloat { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview/spacing)*