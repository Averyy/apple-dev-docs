# CAEmitterLayer

**Framework**: Core Animation  
**Kind**: class

A layer that emits, animates, and renders a particle system.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAEmitterLayer
```

#### Overview

The particles, defined by instances of [`CAEmitterCell`](caemittercell.md), are drawn above the layer’s background color and border.

The following code shows how to set up a simple point (the default [`emitterShape`](caemitterlayer/emittershape.md) is [`point`](caemitterlayeremittershape/point.md)) particle emitter. It uses an image named `RadialGradient.png` as the cell contents and, by setting the emitter cell’s [`emissionRange`](caemittercell/emissionrange.md) to `2 x` doc://com.apple.documentation/documentation/corefoundation/cgfloat/1845230-pi, the particles are emitted in all directions.

```swift
let emitterLayer = CAEmitterLayer()
    
emitterLayer.emitterPosition = CGPoint(x: 320, y: 320)
    
let cell = CAEmitterCell()
cell.birthRate = 100
cell.lifetime = 10
cell.velocity = 100
cell.scale = 0.1
    
cell.emissionRange = CGFloat.pi * 2.0
cell.contents = UIImage(named: "RadialGradient.png")!.cgImage
    
emitterLayer.emitterCells = [cell]
    
view.layer.addSublayer(emitterLayer)
```

## Topics

### Specifying Particle Emitter Cells
- [var emitterCells: [CAEmitterCell]?](caemitterlayer/emittercells.md)
  The array emitter cells attached to the layer.
### Emitter Geometry
- [var renderMode: CAEmitterLayerRenderMode](caemitterlayer/rendermode.md)
  Defines how particle cells are rendered into the layer.
- [var emitterPosition: CGPoint](caemitterlayer/emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterShape: CAEmitterLayerEmitterShape](caemitterlayer/emittershape.md)
  Specifies the emitter shape.
- [var emitterZPosition: CGFloat](caemitterlayer/emitterzposition.md)
  Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [var emitterDepth: CGFloat](caemitterlayer/emitterdepth.md)
  Determines the depth of the emitter shape.
- [var emitterSize: CGSize](caemitterlayer/emittersize.md)
  Determines the size of the particle emitter shape. Animatable.
### Emitter Cell Attribute Multipliers
- [var scale: Float](caemitterlayer/scale.md)
  Defines a multiplier applied to the cell-defined particle scale.
- [var seed: UInt32](caemitterlayer/seed.md)
  Specifies the seed used to initialize the random number generator.
- [var spin: Float](caemitterlayer/spin.md)
  Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [var velocity: Float](caemitterlayer/velocity.md)
  Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [var birthRate: Float](caemitterlayer/birthrate.md)
  Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [var emitterMode: CAEmitterLayerEmitterMode](caemitterlayer/emittermode.md)
  Specifies the emitter mode.
- [var lifetime: Float](caemitterlayer/lifetime.md)
  Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [var preservesDepth: Bool](caemitterlayer/preservesdepth.md)
  Defines whether the layer flattens the particles into its plane.
### Constants
- [Emitter Shape](emitter-shape.md)
  The emission shape is a one, two or three dimensional shape that defines where the emitted particles originate. The shapes are defined by a subset of [`emitterPosition`](caemitterlayer/emitterposition.md), [`emitterZPosition`](caemitterlayer/emitterzposition.md), [`emitterSize`](caemitterlayer/emittersize.md) and [`emitterDepth`](caemitterlayer/emitterdepth.md) properties.
- [Emitter Modes](emitter-modes.md)
  These constants specify the possible emitter modes. They are used by the [`emitterMode`](caemitterlayer/emittermode.md) property.
- [Emitter Render Order](emitter-render-order.md)
  These constants specify the order that emitter cells are composited. They are used by the [`renderMode`](caemitterlayer/rendermode.md) property.

## Relationships

### Inherits From
- [CALayer](calayer.md)
### Conforms To
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CAEmitterCell](caemittercell.md)
  The definition of a particle emitted by a particle layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer)*