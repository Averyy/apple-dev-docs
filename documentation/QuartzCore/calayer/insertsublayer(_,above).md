# insertSublayer(_:above:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Inserts the specified sublayer above a different sublayer that already belongs to the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func insertSublayer(_ layer: CALayer, above sibling: CALayer?)
```

```objc
- (void) insertSublayer:(CALayer *) layer above:(CALayer *) sibling;
```

#### Discussion

If `sublayer` is not in the receiver’s [`sublayers`](./sublayers.md) array, this method raises an exception.

## Parameters

- `layer`: The sublayer to be inserted into the current layer.
- `sibling`: An existing sublayer in the current layer. The layer in `aLayer` is inserted after this layer in the [`sublayers`](./sublayers.md) array, and thus appears in front of it visually.

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
- [func replaceSublayer(CALayer, with: CALayer)](./replacesublayer%28_,with%29.md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/insertsublayer(_:above:))*