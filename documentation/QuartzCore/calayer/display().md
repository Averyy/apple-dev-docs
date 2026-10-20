# display()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Reloads the content of this layer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func display()
```

```objc
- (void) display;
```

#### Discussion

Do not call this method directly. The layer calls this method at appropriate times to update the layer’s content. If the layer has a delegate object, this method attempts to call the delegate’s [`display(_:)`](../calayerdelegate/display%28_%29.md) method, which the delegate can use to update the layer’s contents. If the delegate does not implement the [`display(_:)`](../calayerdelegate/display%28_%29.md) method, this method creates a backing store and calls the layer’s [`draw(in:)`](./draw%28in%29.md) method to fill that backing store with content. The new backing store replaces the previous contents of the layer.

Subclasses can override this method and use it to set the layer’s [`contents`](./contents.md) property directly. You might do this if your custom layer subclass handles layer updates differently.

## See Also

### Providing the layer’s content
- [var contents: Any?](./contents.md)
  An object that provides the contents of the layer. Animatable.
- [var contentsRect: CGRect](./contentsrect.md)
  The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [var contentsCenter: CGRect](./contentscenter.md)
  The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [func draw(in: CGContext)](./draw%28in%29.md)
  Draws the layer’s content using the specified graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/display())*