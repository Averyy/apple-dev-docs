# sublayers

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

An array containing the layer’s sublayers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sublayers: [CALayer]? { get set }
```

```objc
@property (copy, nullable) NSArray<__kindof CALayer *> * sublayers;
```

## Discussion

The sublayers are listed in back to front order. The default value of this property is `nil`.

### Special Considerations

When setting the [`sublayers`](./sublayers.md) property to an array populated with layer objects, each layer in the array must not already have a superlayer—that is, its [`superlayer`](./superlayer.md) property must currently be `nil`.

## See Also

### Managing the layer hierarchy
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
- [func replaceSublayer(CALayer, with: CALayer)](./replacesublayer%28_,with%29.md)
  Replaces the specified sublayer with a different layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/sublayers)*