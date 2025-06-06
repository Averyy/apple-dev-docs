# setRenderingIntent(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets the rendering intent in the current graphics state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setRenderingIntent(_ intent: CGColorRenderingIntent)
```

#### Discussion

The rendering intent specifies how to handle colors that are not located within the gamut of the destination color space of a graphics context. If you do not explicitly set the rendering intent, Core Graphics uses perceptual rendering intent when drawing sampled images and relative colorimetric rendering intent for all other drawing.

## Parameters

- `intent`: A rendering intent constant— ,  ,  ,  , or  . For a discussion of these constants, see  .

## See Also

- [func flush()](cgcontext/flush.md)
  Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [func synchronize()](cgcontext/synchronize.md)
  Marks a window context for update.
- [func setBlendMode(CGBlendMode)](cgcontext/setblendmode(_:).md)
  Sets how sample values are composited by a graphics context.
- [enum CGBlendMode](cgblendmode.md)
  Compositing operations for images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setrenderingintent(_:))*