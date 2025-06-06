# insertSublayer(_:below:)

**Framework**: Core Animation  
**Kind**: method

Inserts the specified sublayer below a different sublayer that already belongs to the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func insertSublayer(_ layer: CALayer, below sibling: CALayer?)
```

#### Discussion

If `sublayer` is not in the receiver’s [`sublayers`](calayer/sublayers.md) array, this method raises an exception.

## Parameters

- `layer`: The sublayer to be inserted into the current layer.
- `sibling`: An existing sublayer in the current layer. The layer in   is inserted before this layer in the   array, and thus appears behind it visually.

## See Also

- [var sublayers: [CALayer]?](calayer/sublayers.md)
  An array containing the layer’s sublayers.
- [var superlayer: CALayer?](calayer/superlayer.md)
  The superlayer of the layer.
- [func addSublayer(CALayer)](calayer/addsublayer(_:).md)
  Appends the layer to the layer’s list of sublayers.
- [func removeFromSuperlayer()](calayer/removefromsuperlayer.md)
  Detaches the layer from its parent layer.
- [func insertSublayer(CALayer, at: UInt32)](calayer/insertsublayer(_:at:).md)
  Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [func insertSublayer(CALayer, above: CALayer?)](calayer/insertsublayer(_:above:).md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [func replaceSublayer(CALayer, with: CALayer)](calayer/replacesublayer(_:with:).md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/insertsublayer(_:below:))*