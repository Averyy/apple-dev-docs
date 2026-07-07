# applyTransform(_:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Transforms this element with the specified transform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func applyTransform(_ transform: CGAffineTransform)
```

## Parameters

- `transform`: The transform applied to the element. Skew is ignored.

## See Also

- [var frame: CGRect](markup/frame.md)
  The element’s unrotated frame.
- [var rotation: CGFloat](markup/rotation.md)
  The element’s rotation around the center of its frame.
- [var renderFrame: CGRect](markup/renderframe.md)
  The unrotated frame that tightly fits the rendered contents of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/applytransform(_:))*