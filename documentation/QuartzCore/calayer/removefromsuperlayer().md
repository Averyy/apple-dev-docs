# removeFromSuperlayer()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeFromSuperlayer;
```

#### Discussion

You can use this method to remove a layer (and all of its sublayers) from a layer hierarchy. This method updates both the superlayer’s list of sublayers and sets this layer’s [`superlayer`](./superlayer.md) property to `nil`.

## See Also

### Managing the layer hierarchy
- [var sublayers: [CALayer]?](./sublayers.md)
  An array containing the layer’s sublayers.
- [var superlayer: CALayer?](./superlayer.md)
  The superlayer of the layer.
- [func addSublayer(CALayer)](./addsublayer%28_%29.md)
  Appends the layer to the layer’s list of sublayers.
- [func insertSublayer(CALayer, at: UInt32)](./insertsublayer%28_,at%29.md)
  Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [func insertSublayer(CALayer, below: CALayer?)](./insertsublayer%28_,below%29.md)
  Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [func insertSublayer(CALayer, above: CALayer?)](./insertsublayer%28_,above%29.md)
  Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [func replaceSublayer(CALayer, with: CALayer)](./replacesublayer%28_,with%29.md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/removefromsuperlayer())*