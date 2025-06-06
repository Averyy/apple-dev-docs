# CAEmitterCell

**Framework**: Core Animation  
**Kind**: class

The definition of a particle emitted by a particle layer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAEmitterCell
```

#### Overview

The [`CAEmitterCell`](caemittercell.md) class represents one source of particles being emitted by a [`CAEmitterLayer`](caemitterlayer.md) object. An emitter cell defines the direction and properties of the emitted particles. Emitter cells can have an array of sub-cells, which lets the particles themselves emit particles.

## Topics

### Providing Emitter Cell Content
- [var contents: Any?](caemittercell/contents.md)
  An object that provides the contents of the layer. Animatable.
- [var contentsRect: CGRect](caemittercell/contentsrect.md)
  A rectangle (in the unit coordinate space) that specifies the portion of [`contents`](caemittercell/contents.md) that the receiver should draw. Animatable.
- [var emitterCells: [CAEmitterCell]?](caemittercell/emittercells.md)
  An optional array containing the sub-cells of this cell.
### Setting Emitter Cell Visual Attributes
- [var isEnabled: Bool](caemittercell/isenabled.md)
  A Boolean value indicating whether or not cells from this emitter are rendered.
- [var color: CGColor?](caemittercell/color.md)
  The color of each emitted object. Animatable.
- [var redRange: Float](caemittercell/redrange.md)
  The amount by which the red color component of the cell can vary. Animatable.
- [var greenRange: Float](caemittercell/greenrange.md)
  The amount by which the green color component of the cell can vary. Animatable.
- [var blueRange: Float](caemittercell/bluerange.md)
  The amount by which the blue color component of the cell can vary. Animatable.
- [var alphaRange: Float](caemittercell/alpharange.md)
  The amount by which the alpha component of the cell can vary. Animatable.
- [var redSpeed: Float](caemittercell/redspeed.md)
  The speed, in seconds, at which the red color component changes over the lifetime of the cell. Animatable.
- [var greenSpeed: Float](caemittercell/greenspeed.md)
  The speed, in seconds, at which the green color component changes over the lifetime of the cell. Animatable.
- [var blueSpeed: Float](caemittercell/bluespeed.md)
  The speed, in seconds, at which the blue color component changes over the lifetime of the cell. Animatable.
- [var alphaSpeed: Float](caemittercell/alphaspeed.md)
  The speed, in seconds, at which the alpha component changes over the lifetime of the cell. Animatable.
- [var magnificationFilter: String](caemittercell/magnificationfilter.md)
  The filter used when increasing the size of the content.
- [var minificationFilter: String](caemittercell/minificationfilter.md)
  The filter used when reducing the size of the content.
- [var minificationFilterBias: Float](caemittercell/minificationfilterbias.md)
  The bias factor used by the minification filter to determine the levels of detail.
- [var scale: CGFloat](caemittercell/scale.md)
  Specifies the scale factor applied to the cell. Animatable.
- [var scaleRange: CGFloat](caemittercell/scalerange.md)
  Specifies the range over which the scale value can vary. Animatable.
- [var contentsScale: CGFloat](caemittercell/contentsscale.md)
  The scale factor of the cell contents.
- [var name: String?](caemittercell/name.md)
  The name of the cell.
- [var style: [AnyHashable : Any]?](caemittercell/style.md)
  An optional dictionary containing additional style values that are not explicitly defined by the receiver.
### Setting Emitter Cell Motion Attributes
- [var spin: CGFloat](caemittercell/spin.md)
  The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [var spinRange: CGFloat](caemittercell/spinrange.md)
  The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [var emissionLatitude: CGFloat](caemittercell/emissionlatitude.md)
  The latitudinal orientation of the emission angle. Animatable.
- [var emissionLongitude: CGFloat](caemittercell/emissionlongitude.md)
  The longitudinal orientation of the emission angle. Animatable.
- [var emissionRange: CGFloat](caemittercell/emissionrange.md)
  The angle, in radians, defining a cone around the emission angle. Animatable.
### Setting Emitter Cell Temporal Attributes
- [var lifetime: Float](caemittercell/lifetime.md)
  The lifetime of the cell, in seconds. Animatable.
- [var lifetimeRange: Float](caemittercell/lifetimerange.md)
  The mean value by which the [`lifetime`](caemittercell/lifetime.md) of the cell can vary. Animatable.
- [var birthRate: Float](caemittercell/birthrate.md)
  The number of emitted objects created every second. Animatable.
- [var scaleSpeed: CGFloat](caemittercell/scalespeed.md)
  The speed at which the scale changes over the lifetime of the cell. Animatable.
- [var velocity: CGFloat](caemittercell/velocity.md)
  The initial velocity of the cell. Animatable.
- [var velocityRange: CGFloat](caemittercell/velocityrange.md)
  The amount by which the velocity of the cell can vary. Animatable.
- [var xAcceleration: CGFloat](caemittercell/xacceleration.md)
  The x component of an acceleration vector applied to cell.
- [var yAcceleration: CGFloat](caemittercell/yacceleration.md)
  The y component of an acceleration vector applied to cell.
- [var zAcceleration: CGFloat](caemittercell/zacceleration.md)
  The z component of an acceleration vector applied to cell.
### Using Key-Value Coding Extensions
- [class func defaultValue(forKey: String) -> Any?](caemittercell/defaultvalue(forkey:).md)
  Returns the default value of the property with the specified key.
- [func shouldArchiveValue(forKey: String) -> Bool](caemittercell/shouldarchivevalue(forkey:).md)
  Returns a Boolean value indicating whether the value for a given key should be archived.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

## See Also

- [class CAEmitterLayer](caemitterlayer.md)
  A layer that emits, animates, and renders a particle system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell)*