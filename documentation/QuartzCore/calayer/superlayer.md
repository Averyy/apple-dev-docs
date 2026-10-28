# superlayer

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) CALayer * superlayer;
```

## Discussion

The superlayer manages the layout of its sublayers.

## See Also

### Managing the layer hierarchy
- [var sublayers: [CALayer]?](./sublayers.md)
  An array containing the layer’s sublayers.
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
- [func replaceSublayer(CALayer, with: CALayer)](./replacesublayer%28_,with%29.md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/superlayer)*