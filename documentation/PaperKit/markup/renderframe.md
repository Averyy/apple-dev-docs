# renderFrame

**Framework**: PaperKit  
**Kind**: property  
**Required**: Yes

The unrotated frame that tightly fits the rendered contents of the element.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderFrame: CGRect { get }
```

#### Discussion

This frame includes padding around `frame` to ensure it includes all the rendered aspects of the content. For example, this frame will include the strokes, and shadows of any contents.

## See Also

- [var frame: CGRect](markup/frame.md)
  The element’s unrotated frame.
- [var rotation: CGFloat](markup/rotation.md)
  The element’s rotation around the center of its frame.
- [func applyTransform(CGAffineTransform)](markup/applytransform(_:).md)
  Transforms this element with the specified transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/renderframe)*