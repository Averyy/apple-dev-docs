# renderFrame

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The unrotated frame that tightly fits the rendered contents of the element.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderFrame: CGRect { get }
```

#### Discussion

This frame includes padding around `frame` to ensure it includes all the rendered aspects of the content. For example, this frame will include the strokes, and shadows of any contents.

## See Also

### Laying out
- [var frame: CGRect](./frame.md)
  The element’s unrotated frame.
- [var rotation: CGFloat](./rotation.md)
  The element’s rotation around the center of its frame.
- [func applyTransform(CGAffineTransform)](./applytransform%28_%29.md)
  Transforms this element with the specified transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/renderframe)*