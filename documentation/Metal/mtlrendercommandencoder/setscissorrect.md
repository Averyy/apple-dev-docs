# setScissorRect(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures a rectangle for the fragment scissor test.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setScissorRect(_ rect: MTLScissorRect)
```

#### Discussion

The rendering pipeline discards any fragments that lie outside the scissor rectangle.

The default scissor rectangle is the same size as the current render attachment, with its origin coordinates in the upper-left corner at `(0, 0)`.

> **Note**:  You can change the render pass’s scissor rectangle configuration by calling this method again or by calling the [`setScissorRects(_:)`](mtlrendercommandencoder/setscissorrects(_:).md) method.

## Parameters

- `rect`: An   instance that represents a rectangle that needs to lie completely within the current render attachment.

## See Also

- [func setViewport(MTLViewport)](mtlrendercommandencoder/setviewport(_:).md)
  Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [func setViewports([MTLViewport])](mtlrendercommandencoder/setviewports(_:).md)
  Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [func setScissorRects([MTLScissorRect])](mtlrendercommandencoder/setscissorrects(_:).md)
  Configures multiple rectangles for the fragment scissor test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setscissorrect(_:))*