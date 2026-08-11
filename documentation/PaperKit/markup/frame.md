# frame

**Framework**: PaperKit  
**Kind**: property  
**Required**: Yes

The element’s unrotated frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var frame: CGRect { get set }
```

#### Discussion

Together with `rotation` this defines the element’s position in its parent. This won’t necessarily contain all the contents of an element, rotation and styling may cause the element to extend beyond this frame. Use `renderFrame` for an unrotated frame that contains the entire element.

## See Also

- [var rotation: CGFloat](markup/rotation.md)
  The element’s rotation around the center of its frame.
- [var renderFrame: CGRect](markup/renderframe.md)
  The unrotated frame that tightly fits the rendered contents of the element.
- [func applyTransform(CGAffineTransform)](markup/applytransform(_:).md)
  Transforms this element with the specified transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/frame)*