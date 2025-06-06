# magnificationFilter

**Framework**: Core Animation  
**Kind**: property

The filter used when increasing the size of the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var magnificationFilter: CALayerContentsFilter { get set }
```

#### Discussion

The possible values for this property are listed in [`Scaling Filters`](scaling-filters.md).

The default value of this property is [`linear`](calayercontentsfilter/linear.md).

[`Figure 1`](calayer/1410907-magnificationfilter#2851435.md) shows the difference between linear and nearest filtering when a 10 x 10 point image of a circle is magnified by a scale of 10.

![Circle with different magnification filters](https://docs-assets.developer.apple.com/published/c00f9e57718120dafa9ff73959f5b0df/media-2851435%402x.png)

The circle on the left uses [`linear`](calayercontentsfilter/linear.md) and the circle on the right uses [`nearest`](calayercontentsfilter/nearest.md).

## See Also

- [var filters: [Any]?](calayer/filters.md)
  An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [var compositingFilter: Any?](calayer/compositingfilter.md)
  A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [var backgroundFilters: [Any]?](calayer/backgroundfilters.md)
  An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [var minificationFilter: CALayerContentsFilter](calayer/minificationfilter.md)
  The filter used when reducing the size of the content.
- [var minificationFilterBias: Float](calayer/minificationfilterbias.md)
  The bias factor used by the minification filter to determine the levels of detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/magnificationfilter)*