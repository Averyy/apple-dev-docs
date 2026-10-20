# scale

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property CGFloat scale;
```

#### Discussion

The scale of the cell will vary by a random amount within the range specified by [`scaleRange`](./scalerange.md). The [`scaleSpeed`](./scalespeed.md) property determines the rate of change.

The default value of this property is `1.0`.

## See Also

### Related Documentation
- [var scaleSpeed: CGFloat](./scalespeed.md)
  The speed at which the scale changes over the lifetime of the cell. Animatable.
### Setting Emitter Cell Visual Attributes
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether or not cells from this emitter are rendered.
- [var color: CGColor?](./color.md)
  The color of each emitted object. Animatable.
- [var redRange: Float](./redrange.md)
  The amount by which the red color component of the cell can vary. Animatable.
- [var greenRange: Float](./greenrange.md)
  The amount by which the green color component of the cell can vary. Animatable.
- [var blueRange: Float](./bluerange.md)
  The amount by which the blue color component of the cell can vary. Animatable.
- [var alphaRange: Float](./alpharange.md)
  The amount by which the alpha component of the cell can vary. Animatable.
- [var redSpeed: Float](./redspeed.md)
  The speed, in seconds, at which the red color component changes over the lifetime of the cell. Animatable.
- [var greenSpeed: Float](./greenspeed.md)
  The speed, in seconds, at which the green color component changes over the lifetime of the cell. Animatable.
- [var blueSpeed: Float](./bluespeed.md)
  The speed, in seconds, at which the blue color component changes over the lifetime of the cell. Animatable.
- [var alphaSpeed: Float](./alphaspeed.md)
  The speed, in seconds, at which the alpha component changes over the lifetime of the cell. Animatable.
- [var magnificationFilter: String](./magnificationfilter.md)
  The filter used when increasing the size of the content.
- [var minificationFilter: String](./minificationfilter.md)
  The filter used when reducing the size of the content.
- [var minificationFilterBias: Float](./minificationfilterbias.md)
  The bias factor used by the minification filter to determine the levels of detail.
- [var scaleRange: CGFloat](./scalerange.md)
  Specifies the range over which the scale value can vary. Animatable.
- [var contentsScale: CGFloat](./contentsscale.md)
  The scale factor of the cell contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/scale)*