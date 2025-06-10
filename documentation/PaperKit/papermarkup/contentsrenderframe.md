# contentsRenderFrame

**Framework**: PaperKit  
**Kind**: property

The frame that tightly fits the rendered contents on the paper.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var contentsRenderFrame: CGRect { get }
```

#### Discussion

This frame includes padding around `contentsFrame` to ensure it includes all the rendered aspects of the content. For example, this frame will include the strokes, and shadows of any contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/contentsrenderframe)*