# draw(_:in:)

**Framework**: Core Animation  
**Kind**: method

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

#### Discussion

The [`draw(_:in:)`](calayerdelegate/draw(_:in:).md) method is called when the layer is marked for its content to be reloaded, typically with the [`setNeedsDisplay()`](calayer/setneedsdisplay().md) method. It is not called if the delegate implements the [`display(_:)`](calayerdelegate/display(_:).md) method. You can use the context to draw vectors, such as curves and lines, or images with the [`draw(_:in:byTiling:)`](https://developer.apple.com/documentation/CoreGraphics/CGContext/draw(_:in:byTiling:)) method.

The following code shows how you can create a class named `LayerDelegate` that implements [`CALayerDelegate`](calayerdelegate.md) and sets it as a layer’s (named `sublayer`) delegate. When [`setNeedsDisplay()`](calayer/setneedsdisplay().md) is called on `sublayer`, the delegate’s [`draw(_:in:)`](calayerdelegate/draw(_:in:).md) method draws an ellipse fitting the bounding box of the layer using the [`boundingBoxOfClipPath`](https://developer.apple.com/documentation/CoreGraphics/CGContext/boundingBoxOfClipPath) function.

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

> ❗ **Important**:  This method is not called if the delegate implements [`display(_:)`](calayerdelegate/display(_:).md).

## Parameters

- `layer`: The layer whose contents need to be drawn.
- `ctx`: The graphics context to use for drawing. The graphics context incorporates the appropriate scale factor for drawing to the target screen.

## See Also

- [func display(CALayer)](calayerdelegate/display(_:).md)
  Tells the delegate to implement the display process.
- [func layerWillDraw(CALayer)](calayerdelegate/layerwilldraw(_:).md)
  Notifies the delegate of an imminent draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayerdelegate/draw(_:in:))*