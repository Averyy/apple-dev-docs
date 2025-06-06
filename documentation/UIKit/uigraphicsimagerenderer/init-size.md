# init(size:)

**Framework**: UIKit  
**Kind**: init

Creates an image renderer for drawing images of the specified size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(size: CGSize)
```

#### Return Value

An initialized image renderer.

#### Discussion

Use this initializer to create an image renderer that will draw images of a given size. This renderer uses the [`default()`](uigraphicsrendererformat/default().md) static method on [`UIGraphicsImageRendererContext`](uigraphicsimagerenderercontext.md) to create its context, thereby selecting parameters that are the most appropriate for the current device.

## Parameters

- `size`: The size of images output from the renderer, specified in points.

## See Also

- [init(bounds: CGRect, format: UIGraphicsImageRendererFormat)](uigraphicsimagerenderer/init(bounds:format:).md)
  Creates an image renderer with the specified bounds and format.
- [init(size: CGSize, format: UIGraphicsImageRendererFormat)](uigraphicsimagerenderer/init(size:format:).md)
  Creates an image renderer with the specified size and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(size:))*