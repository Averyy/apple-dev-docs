# frame

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The element’s unrotated frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var frame: CGRect { get set }
```

#### Discussion

Together with `rotation` this defines the element’s position in its parent. This won’t necessarily contain all the contents of an element, rotation and styling may cause the element to extend beyond this frame. Use `renderFrame` for an unrotated frame that contains the entire element.

## See Also

### Laying out
- [var rotation: CGFloat](./rotation.md)
  The element’s rotation around the center of its frame.
- [var renderFrame: CGRect](./renderframe.md)
  The unrotated frame that tightly fits the rendered contents of the element.
- [func applyTransform(CGAffineTransform)](./applytransform%28_%29.md)
  Transforms this element with the specified transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/frame)*