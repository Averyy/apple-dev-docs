# render(rasterizationScale:renderer:)

**Framework**: SwiftUI  
**Kind**: method

Draws the renderer’s current contents to an arbitrary Core Graphics context.

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
final func render(rasterizationScale: CGFloat = 1, renderer: (CGSize, (CGContext) -> Void) -> Void)
```

#### Discussion

Use this method to rasterize the renderer’s content to a [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) you provide. The `renderer` closure receives two parameters: the current size of the view, and a function that renders the view to your `CGContext`. Implement the closure to provide a suitable `CGContext`, then invoke the function to render the content to that context.

## Parameters

- `rasterizationScale`: The scale factor for converting user   interface points to pixels when rasterizing parts of the   view that can’t be represented as native Core Graphics drawing   commands.
- `renderer`: The closure that sets up the Core Graphics context and   renders the view. This closure receives two parameters: the size of   the view and a function that you invoke in the closure to render the   view at the reported size. This function takes a     parameter, and assumes a bottom-left coordinate space origin.

## See Also

- [var cgImage: CGImage?](imagerenderer/cgimage.md)
  The current contents of the view, rasterized as a Core Graphics image.
- [var nsImage: NSImage?](imagerenderer/nsimage.md)
  The current contents of the view, rasterized as an AppKit image.
- [var uiImage: UIImage?](imagerenderer/uiimage.md)
  The current contents of the view, rasterized as a UIKit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/render(rasterizationscale:renderer:))*