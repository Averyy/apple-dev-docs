# draw(in:)

**Framework**: Core Animation  
**Kind**: method

Draws the layer’s content using the specified graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func draw(in ctx: CGContext)
```

#### Discussion

The default implementation of this method does not do any drawing itself. If the layer’s delegate implements the  [`draw(_:in:)`](calayerdelegate/draw(_:in:).md) method, that method is called to do the actual drawing.

Subclasses can override this method and use it to draw the layer’s content. When drawing, all coordinates should be specified in points in the logical coordinate space.

## Parameters

- `ctx`: The graphics context in which to draw the content. The context may be clipped to protect valid layer content. Subclasses that wish to find the actual region to draw can call  .

## See Also

- [var contents: Any?](calayer/contents.md)
  An object that provides the contents of the layer. Animatable.
- [var contentsRect: CGRect](calayer/contentsrect.md)
  The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [var contentsCenter: CGRect](calayer/contentscenter.md)
  The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [func display()](calayer/display.md)
  Reloads the content of this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/draw(in:))*