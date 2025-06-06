# removeFromSuperlayer()

**Framework**: Core Animation  
**Kind**: method

Detaches the layer from its parent layer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromSuperlayer()
```

#### Discussion

You can use this method to remove a layer (and all of its sublayers) from a layer hierarchy. This method updates both the superlayer’s list of sublayers and sets this layer’s [`superlayer`](calayer/superlayer.md) property to `nil`.

## See Also

- [var sublayers: [CALayer]?](calayer/sublayers.md)
  An array containing the layer’s sublayers.
- [var superlayer: CALayer?](calayer/superlayer.md)
  The superlayer of the layer.
- [func addSublayer(CALayer)](calayer/addsublayer(_:).md)
  Appends the layer to the layer’s list of sublayers.
- [func insertSublayer(CALayer, at: UInt32)](calayer/insertsublayer(_:at:).md)
  Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [func insertSublayer(CALayer, below: CALayer?)](calayer/insertsublayer(_:below:).md)
  Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [func insertSublayer(CALayer, above: CALayer?)](calayer/insertsublayer(_:above:).md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [func replaceSublayer(CALayer, with: CALayer)](calayer/replacesublayer(_:with:).md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/removefromsuperlayer())*