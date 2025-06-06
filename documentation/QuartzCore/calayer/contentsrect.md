# contentsRect

**Framework**: Core Animation  
**Kind**: property

The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentsRect: CGRect { get set }
```

#### Discussion

Defaults to the unit rectangle (0.0, 0.0, 1.0, 1.0).

If pixels outside the unit rectangle are requested, the edge pixels of the contents image will be extended outwards.

If an empty rectangle is provided, the results are undefined.

## See Also

- [var contents: Any?](calayer/contents.md)
  An object that provides the contents of the layer. Animatable.
- [var contentsCenter: CGRect](calayer/contentscenter.md)
  The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [func display()](calayer/display.md)
  Reloads the content of this layer.
- [func draw(in: CGContext)](calayer/draw(in:).md)
  Draws the layer’s content using the specified graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contentsrect)*