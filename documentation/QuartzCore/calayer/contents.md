# contents

**Framework**: Core Animation  
**Kind**: property

An object that provides the contents of the layer. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contents: Any? { get set }
```

#### Discussion

The default value of this property is `nil`.

If you are using the layer to display a static image, you can set this property to the [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) containing the image you want to display. (In macOS 10.6 and later, you can also set the property to an [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) object.) Assigning a value to this property causes the layer to use your image rather than create a separate backing store.

If the layer object is tied to a view object, you should avoid setting the contents of this property directly. The interplay between views and layers usually results in the view replacing the contents of this property during a subsequent update.

## See Also

- [var contentsRect: CGRect](calayer/contentsrect.md)
  The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [var contentsCenter: CGRect](calayer/contentscenter.md)
  The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [func display()](calayer/display.md)
  Reloads the content of this layer.
- [func draw(in: CGContext)](calayer/draw(in:).md)
  Draws the layer’s content using the specified graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contents)*