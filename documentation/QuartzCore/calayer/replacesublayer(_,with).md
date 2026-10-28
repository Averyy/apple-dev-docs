# replaceSublayer(_:with:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Replaces the specified sublayer with a different layer object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func replaceSublayer(_ oldLayer: CALayer, with newLayer: CALayer)
```

```objc
- (void) replaceSublayer:(CALayer *) oldLayer with:(CALayer *) newLayer;
```

## Discussion

If `oldLayer` is not in the receiver’s [`sublayers`](./sublayers.md) array, the behavior of this method is undefined.

## Parameters

- `oldLayer`: The layer to be replaced.
- `newLayer`: The layer with which to replace `oldLayer`.

## See Also

### Managing the layer hierarchy
- [var sublayers: [CALayer]?](./sublayers.md)
  An array containing the layer’s sublayers.
- [var superlayer: CALayer?](./superlayer.md)
  The superlayer of the layer.
- [func addSublayer(CALayer)](./addsublayer%28_%29.md)
  Appends the layer to the layer’s list of sublayers.
- [func removeFromSuperlayer()](./removefromsuperlayer%28%29.md)
  Detaches the layer from its parent layer.
- [func insertSublayer(CALayer, at: UInt32)](./insertsublayer%28_,at%29.md)
  Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [func insertSublayer(CALayer, below: CALayer?)](./insertsublayer%28_,below%29.md)
  Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [func insertSublayer(CALayer, above: CALayer?)](./insertsublayer%28_,above%29.md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/replacesublayer(_:with:))*