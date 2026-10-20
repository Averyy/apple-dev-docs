# contents

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (strong, nullable) id contents;
```

#### Discussion

The default value of this property is `nil`.

If you are using the layer to display a static image, you can set this property to the [`CGImage`](../../CoreGraphics/cgimage.md) containing the image you want to display. (In macOS 10.6 and later, you can also set the property to an [`NSImage`](../../AppKit/nsimage.md) object.) Assigning a value to this property causes the layer to use your image rather than create a separate backing store.

If the layer object is tied to a view object, you should avoid setting the contents of this property directly. The interplay between views and layers usually results in the view replacing the contents of this property during a subsequent update.

## See Also

### Providing the layer’s content
- [var contentsRect: CGRect](./contentsrect.md)
  The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [var contentsCenter: CGRect](./contentscenter.md)
  The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [func display()](./display%28%29.md)
  Reloads the content of this layer.
- [func draw(in: CGContext)](./draw%28in%29.md)
  Draws the layer’s content using the specified graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contents)*