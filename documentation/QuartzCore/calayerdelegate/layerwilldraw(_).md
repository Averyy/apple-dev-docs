# layerWillDraw(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate of an imminent draw.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func layerWillDraw(_ layer: CALayer)
```

```objc
- (void) layerWillDraw:(CALayer *) layer;
```

## Discussion

The [`layerWillDraw(_:)`](./layerwilldraw%28_%29.md) method is called before [`draw(_:in:)`](./draw%28_,in%29.md). You can use this method to configure any layer state affecting contents prior to [`draw(_:in:)`](./draw%28_,in%29.md) such as [`contentsFormat`](../calayer/contentsformat.md) and [`isOpaque`](../calayer/isopaque.md).

> ❗ **Important**:  This method is not called if the delegate implements [`display(_:)`](./display%28_%29.md).

## Parameters

- `layer`: The layer whose contents will be drawn.

## See Also

### Providing the Layer’s Content
- [func display(CALayer)](./display%28_%29.md)
  Tells the delegate to implement the display process.
- [func draw(CALayer, in: CGContext)](./draw%28_,in%29.md)
  Tells the delegate to implement the display process using the layer’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayerdelegate/layerwilldraw(_:))*