# init(bounds:format:)

**Framework**: UIKit  
**Kind**: init

Creates an image renderer with the specified bounds and format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(bounds: CGRect, format: UIGraphicsImageRendererFormat)
```

#### Return Value

An initialized image renderer.

#### Discussion

Use this initializer to create an image renderer when you want to override the default format for the current device.

## Parameters

- `bounds`: The bounds of the image context the image renderer creates and subsequently draws upon. Specify values in points in the Core Graphics coordinate space.
- `format`: A   object that encapsulates the format used to create the renderer context.

## See Also

- [convenience init(size: CGSize)](uigraphicsimagerenderer/init(size:).md)
  Creates an image renderer for drawing images of the specified size.
- [init(size: CGSize, format: UIGraphicsImageRendererFormat)](uigraphicsimagerenderer/init(size:format:).md)
  Creates an image renderer with the specified size and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(bounds:format:))*