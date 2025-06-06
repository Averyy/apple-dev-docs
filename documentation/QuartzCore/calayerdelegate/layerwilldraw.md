# layerWillDraw(_:)

**Framework**: Core Animation  
**Kind**: method

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

#### Discussion

The [`layerWillDraw(_:)`](calayerdelegate/layerwilldraw(_:).md) method is called before [`draw(_:in:)`](calayerdelegate/draw(_:in:).md). You can use this method to configure any layer state affecting contents prior to [`draw(_:in:)`](calayerdelegate/draw(_:in:).md) such as [`contentsFormat`](calayer/contentsformat.md) and [`isOpaque`](calayer/isopaque.md).

> ❗ **Important**:  This method is not called if the delegate implements [`display(_:)`](calayerdelegate/display(_:).md).

 This method is not called if the delegate implements [`display(_:)`](calayerdelegate/display(_:).md).

## Parameters

- `layer`: The layer whose contents will be drawn.

## See Also

- [func display(CALayer)](calayerdelegate/display(_:).md)
  Tells the delegate to implement the display process.
- [func draw(CALayer, in: CGContext)](calayerdelegate/draw(_:in:).md)
  Tells the delegate to implement the display process using the layer’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayerdelegate/layerwilldraw(_:))*