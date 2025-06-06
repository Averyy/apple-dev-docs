# scale

**Framework**: Core Animation  
**Kind**: property

Specifies the scale factor applied to the cell. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var scale: CGFloat { get set }
```

#### Discussion

The scale of the cell will vary by a random amount within the range specified by [`scaleRange`](caemittercell/scalerange.md). The [`scaleSpeed`](caemittercell/scalespeed.md) property determines the rate of change.

The default value of this property is `1.0`.

## See Also

- [var scaleSpeed: CGFloat](caemittercell/scalespeed.md)
  The speed at which the scale changes over the lifetime of the cell. Animatable.
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
- [var scaleRange: CGFloat](caemittercell/scalerange.md)
  Specifies the range over which the scale value can vary. Animatable.
- [var contentsScale: CGFloat](caemittercell/contentsscale.md)
  The scale factor of the cell contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/scale)*