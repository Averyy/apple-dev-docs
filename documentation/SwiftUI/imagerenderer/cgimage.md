# cgImage

**Framework**: SwiftUI  
**Kind**: property

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

- [func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) -> Void) -> Void)](imagerenderer/render(rasterizationscale:renderer:).md)
  Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [var nsImage: NSImage?](imagerenderer/nsimage.md)
  The current contents of the view, rasterized as an AppKit image.
- [var uiImage: UIImage?](imagerenderer/uiimage.md)
  The current contents of the view, rasterized as a UIKit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/cgimage)*