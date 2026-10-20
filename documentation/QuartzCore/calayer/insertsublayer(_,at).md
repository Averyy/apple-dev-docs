# insertSublayer(_:at:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Inserts the specified layer into the receiver’s list of sublayers at the specified index.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func insertSublayer(_ layer: CALayer, at idx: UInt32)
```

```objc
- (void) insertSublayer:(CALayer *) layer atIndex:(unsigned int) idx;
```

## Parameters

- `layer`: The sublayer to be inserted into the current layer.
- `idx`: The index at which to insert `aLayer`. This value must be a valid 0-based index into the [`sublayers`](./sublayers.md) array.

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
- [func insertSublayer(CALayer, below: CALayer?)](./insertsublayer%28_,below%29.md)
  Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [func insertSublayer(CALayer, above: CALayer?)](./insertsublayer%28_,above%29.md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [func replaceSublayer(CALayer, with: CALayer)](./replacesublayer%28_,with%29.md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/insertsublayer(_:at:))*