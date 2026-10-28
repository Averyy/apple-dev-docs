# init(size:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSize:(CGSize) size;
```

## Return Value

An initialized image renderer.

## Discussion

Use this initializer to create an image renderer that will draw images of a given size. This renderer uses the [`default()`](../uigraphicsrendererformat/default%28%29.md) static method on [`UIGraphicsImageRendererContext`](../uigraphicsimagerenderercontext.md) to create its context, thereby selecting parameters that are the most appropriate for the current device.

## Parameters

- `size`: The size of images output from the renderer, specified in points.

## See Also

### Initializing an image renderer
- [init(bounds: CGRect, format: UIGraphicsImageRendererFormat)](./init%28bounds,format%29.md)
  Creates an image renderer with the specified bounds and format.
- [init(size: CGSize, format: UIGraphicsImageRendererFormat)](./init%28size,format%29.md)
  Creates an image renderer with the specified size and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/init(size:))*