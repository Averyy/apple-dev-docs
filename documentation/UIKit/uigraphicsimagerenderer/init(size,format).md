# init(size:format:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an image renderer with the specified size and format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(size: CGSize, format: UIGraphicsImageRendererFormat)
```

```objc
- (instancetype) initWithSize:(CGSize) size format:(UIGraphicsImageRendererFormat *) format;
```

## Return Value

An initialized renderer.

## Discussion

Use this initializer to create an image renderer when you want to override the default format for the current device. Provide the size of the images you want to create, and an instance of [`UIGraphicsImageRendererFormat`](../uigraphicsimagerendererformat.md) with the required configuration.

## Parameters

- `size`: The size of images output from the renderer, specified in points.
- `format`: A [`UIGraphicsImageRendererFormat`](../uigraphicsimagerendererformat.md) object that encapsulates the format used to create the renderer context.

## See Also

### Initializing an image renderer
- [init(bounds: CGRect, format: UIGraphicsImageRendererFormat)](./init%28bounds,format%29.md)
  Creates an image renderer with the specified bounds and format.
- [convenience init(size: CGSize)](./init%28size%29.md)
  Creates an image renderer for drawing images of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(size:format:))*