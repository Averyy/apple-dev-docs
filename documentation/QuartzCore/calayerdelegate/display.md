# display(_:)

**Framework**: Core Animation  
**Kind**: method

Tells the delegate to implement the display process.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func display(_ layer: CALayer)
```

#### Discussion

The [`display(_:)`](calayerdelegate/display(_:).md) delegate method is called when the layer is marked for its content to be reloaded, typically initiated by the [`setNeedsDisplay()`](calayer/setneedsdisplay().md) method. The typical technique for updating is to set the layer’s `contents` property.

The following code shows how you can create a class named `LayerDelegate` that implements [`CALayerDelegate`](calayerdelegate.md) and sets it as a layer’s (named `sublayer`) delegate. When [`setNeedsDisplay()`](calayer/setneedsdisplay().md) is called on `sublayer`, the delegate’s [`display(_:)`](calayerdelegate/display(_:).md) replaces its contents with a specified image.

```swift
let delegate = LayerDelegate()
     
lazy var sublayer: CALayer = {
    let layer = CALayer()
    
    layer.delegate = self.delegate
    
    return layer
}()
     
// When `sublayer.setNeedsDisplay()` is called, `sublayer.contents` are updated.
     
class LayerDelegate: NSObject, CALayerDelegate {
    func display(_ layer: CALayer) {
        layer.contents = UIImage(named: "rabbit.png")?.cgImage
    }
}
```

## Parameters

- `layer`: The layer whose contents need updating.

## See Also

- [func draw(CALayer, in: CGContext)](calayerdelegate/draw(_:in:).md)
  Tells the delegate to implement the display process using the layer’s context.
- [func layerWillDraw(CALayer)](calayerdelegate/layerwilldraw(_:).md)
  Notifies the delegate of an imminent draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayerdelegate/display(_:))*