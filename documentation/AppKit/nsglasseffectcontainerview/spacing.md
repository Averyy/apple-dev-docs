# spacing

**Framework**: AppKit  
**Kind**: property

The proximity at which the glass effect container view begins merging eligible descendent glass effect views.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var spacing: CGFloat { get set }
```

#### Discussion

The default value, zero, is sufficient for batch processing eligible glass effect views, while avoiding distortion and merging effects for other views in close proximity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview/spacing)*