# superlayer

**Framework**: Core Animation  
**Kind**: property

The superlayer of the layer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var superlayer: CALayer? { get }
```

#### Discussion

The superlayer manages the layout of its sublayers.

## See Also

- [var sublayers: [CALayer]?](calayer/sublayers.md)
  An array containing the layer’s sublayers.
- [func addSublayer(CALayer)](calayer/addsublayer(_:).md)
  Appends the layer to the layer’s list of sublayers.
- [func removeFromSuperlayer()](calayer/removefromsuperlayer.md)
  Detaches the layer from its parent layer.
- [func insertSublayer(CALayer, at: UInt32)](calayer/insertsublayer(_:at:).md)
  Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [func insertSublayer(CALayer, below: CALayer?)](calayer/insertsublayer(_:below:).md)
  Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [func insertSublayer(CALayer, above: CALayer?)](calayer/insertsublayer(_:above:).md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [func replaceSublayer(CALayer, with: CALayer)](calayer/replacesublayer(_:with:).md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/superlayer)*