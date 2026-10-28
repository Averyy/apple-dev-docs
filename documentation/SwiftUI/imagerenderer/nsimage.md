# nsImage

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The current contents of the view, rasterized as an AppKit image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var nsImage: NSImage? { get }
```

Available when `Content` conforms to `View`.

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of the image may have changed.

## See Also

### Rendering images
- [func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) -> Void) -> Void)](./render%28rasterizationscale,renderer%29.md)
  Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [var cgImage: CGImage?](./cgimage.md)
  The current contents of the view, rasterized as a Core Graphics image.
- [var uiImage: UIImage?](./uiimage.md)
  The current contents of the view, rasterized as a UIKit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/nsimage)*