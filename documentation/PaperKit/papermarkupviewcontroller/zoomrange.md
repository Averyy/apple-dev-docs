# zoomRange

**Framework**: PaperKit  
**Kind**: property

A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var zoomRange: ClosedRange<CGFloat> { get set }
```

#### Discussion

The default value is `1.0...1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/zoomrange)*