# rotation

**Framework**: PaperKit  
**Kind**: property  
**Required**: Yes

The element’s rotation around the center of its frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var rotation: CGFloat { get set }
```

#### Discussion

Together with `frame` this defines the element’s position in its parent.

## See Also

- [var frame: CGRect](markup/frame.md)
  The element’s unrotated frame.
- [var renderFrame: CGRect](markup/renderframe.md)
  The unrotated frame that tightly fits the rendered contents of the element.
- [func applyTransform(CGAffineTransform)](markup/applytransform(_:).md)
  Transforms this element with the specified transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/rotation)*