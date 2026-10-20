# draw(_:in:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to implement the display process using the layer’s context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func draw(_ layer: CALayer, in ctx: CGContext)
```

```objc
- (void) drawLayer:(CALayer *) layer inContext:(CGContextRef) ctx;
```

#### Discussion

The [`draw(_:in:)`](./draw%28_,in%29.md) method is called when the layer is marked for its content to be reloaded, typically with the [`setNeedsDisplay()`](../calayer/setneedsdisplay%28%29.md) method. It is not called if the delegate implements the [`display(_:)`](./display%28_%29.md) method. You can use the context to draw vectors, such as curves and lines, or images with the [`draw(_:in:byTiling:)`](../../CoreGraphics/cgcontext/draw%28_,in,bytiling%29.md) method.

The following code shows how you can create a class named `LayerDelegate` that implements [`CALayerDelegate`](../calayerdelegate.md) and sets it as a layer’s (named `sublayer`) delegate. When [`setNeedsDisplay()`](../calayer/setneedsdisplay%28%29.md) is called on `sublayer`, the delegate’s [`draw(_:in:)`](./draw%28_,in%29.md) method draws an ellipse fitting the bounding box of the layer using the [`boundingBoxOfClipPath`](../../CoreGraphics/cgcontext/boundingboxofclippath.md) function.

```swift
let delegate = LayerDelegate()
    
lazy var sublayer: CALayer = {
    let layer = CALayer()
    
    layer.delegate = self.delegate
    
    return layer
}()
    
// sublayer.setNeedsDisplay()
    
class LayerDelegate: NSObject, CALayerDelegate {
    func draw(_ layer: CALayer, in ctx: CGContext) {
        ctx.addEllipse(in: ctx.boundingBoxOfClipPath)
        ctx.strokePath()
    }
}
```

> ❗ **Important**:  This method is not called if the delegate implements [`display(_:)`](./display%28_%29.md).

## Parameters

- `layer`: The layer whose contents need to be drawn.
- `ctx`: The graphics context to use for drawing. The graphics context incorporates the appropriate scale factor for drawing to the target screen.

## See Also

### Providing the Layer’s Content
- [func display(CALayer)](./display%28_%29.md)
  Tells the delegate to implement the display process.
- [func layerWillDraw(CALayer)](./layerwilldraw%28_%29.md)
  Notifies the delegate of an imminent draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayerdelegate/draw(_:in:))*