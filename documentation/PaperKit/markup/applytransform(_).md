# applyTransform(_:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Transforms this element with the specified transform.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func applyTransform(_ transform: CGAffineTransform)
```

## Parameters

- `transform`: The transform applied to the element. Skew is ignored.

## Default Implementations

### Markup Implementations
- [func applyTransform(CGAffineTransform)](./applytransform%28_%29-9je6a.md)
  Transforms this element with the specified transform.

## See Also

### Laying out
- [var frame: CGRect](./frame.md)
  The element’s unrotated frame.
- [var rotation: CGFloat](./rotation.md)
  The element’s rotation around the center of its frame.
- [var renderFrame: CGRect](./renderframe.md)
  The unrotated frame that tightly fits the rendered contents of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/applytransform(_:))*