# emitterCells

**Framework**: Core Animation  
**Kind**: property

An optional array containing the sub-cells of this cell.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterCells: [CAEmitterCell]? { get set }
```

#### Discussion

When specified, each particle emitted by the cell acts as an emitter for each of the cell’s sub-cells. The emission point is the current particle position and the emission angle is relative to the current direction of the particle.

The default value of this property is `nil`.

The following code shows how you can create a firework style effect using sub-cells. The `fireworkCell` has an emission longitude of one quarter turn anti-clockwise to emit particles upwards. It emits `trailCell` instances which have a slight [`yAcceleration`](caemittercell/yacceleration.md) that simulates gravity.

Note that the [`scale`](caemittercell/scale.md) and [`color`](caemittercell/color.md) of `fireworkCell` are inherited by `trailCell`.

Listing 1. Creating particle trails

```swift
let image = UIImage(named: "RadialGradient.png")!.cgImage
    
let emitterLayer = CAEmitterLayer()
    
emitterLayer.emitterPosition = CGPoint(x: 512, y: 512)
    
let fireworkCell = CAEmitterCell()
fireworkCell.color = UIColor.red.cgColor
fireworkCell.birthRate = 3
fireworkCell.lifetime = 10
fireworkCell.velocity = 100
fireworkCell.scale = 0.05
fireworkCell.emissionLongitude = -CGFloat.pi * 0.5
fireworkCell.emissionRange = -CGFloat.pi * 0.25
fireworkCell.contents = image
    
let trailCell = CAEmitterCell()
trailCell.yAcceleration = 20
trailCell.birthRate = 10
trailCell.lifetime = 3
trailCell.contents = image
    
fireworkCell.emitterCells = [trailCell]
emitterLayer.emitterCells = [fireworkCell]
    
view.layer.addSublayer(emitterLayer)
```

## See Also

- [var contents: Any?](caemittercell/contents.md)
  An object that provides the contents of the layer. Animatable.
- [var contentsRect: CGRect](caemittercell/contentsrect.md)
  A rectangle (in the unit coordinate space) that specifies the portion of [`contents`](caemittercell/contents.md) that the receiver should draw. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/emittercells)*