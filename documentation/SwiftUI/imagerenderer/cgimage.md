# cgImage

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The current contents of the view, rasterized as a Core Graphics image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
final var cgImage: CGImage? { get }
```

#### Discussion

The renderer notifies its `objectWillChange` publisher when the contents of the image may have changed.

## See Also

### Rendering images
- [func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) -> Void) -> Void)](./render%28rasterizationscale,renderer%29.md)
  Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [var nsImage: NSImage?](./nsimage.md)
  The current contents of the view, rasterized as an AppKit image.
- [var uiImage: UIImage?](./uiimage.md)
  The current contents of the view, rasterized as a UIKit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/cgimage)*