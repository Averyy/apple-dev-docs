# minificationFilter

**Framework**: Core Animation  
**Kind**: property

The filter used when reducing the size of the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var minificationFilter: CALayerContentsFilter { get set }
```

#### Discussion

The possible values for this property are listed in [`Scaling Filters`](scaling-filters.md).

The default value of this property is [`linear`](calayercontentsfilter/linear.md).

## See Also

- [var filters: [Any]?](calayer/filters.md)
  An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [var compositingFilter: Any?](calayer/compositingfilter.md)
  A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [var backgroundFilters: [Any]?](calayer/backgroundfilters.md)
  An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [var minificationFilterBias: Float](calayer/minificationfilterbias.md)
  The bias factor used by the minification filter to determine the levels of detail.
- [var magnificationFilter: CALayerContentsFilter](calayer/magnificationfilter.md)
  The filter used when increasing the size of the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/minificationfilter)*