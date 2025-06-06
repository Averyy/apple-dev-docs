# tiledImage(_:origin:sourceRect:scale:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that tiles an image across the infinite plane.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func tiledImage(_ image: Image, origin: CGPoint = .zero, sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1), scale: CGFloat = 1) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a tiled image.

## Parameters

- `image`: An   to use as fill.
- `origin`: The point in the current user space where SwiftUI   places the bottom left corner of the part of the image   defined by  . The image repeats as needed.
- `sourceRect`: A unit space subregion of the image. The default   is a unit rectangle, which selects the whole image.
- `scale`: A factor that you can use to control the image size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/tiledimage(_:origin:sourcerect:scale:))*