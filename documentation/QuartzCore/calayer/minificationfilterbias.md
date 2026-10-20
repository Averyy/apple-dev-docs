# minificationFilterBias

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The bias factor used by the minification filter to determine the levels of detail.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var minificationFilterBias: Float { get set }
```

```objc
@property float minificationFilterBias;
```

#### Discussion

This value is used by the [`minificationFilter`](./minificationfilter.md) when it is set to [`trilinear`](../calayercontentsfilter/trilinear.md).

The default value of this property is `0.0`.

## See Also

### Layer filters
- [var filters: [Any]?](./filters.md)
  An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [var compositingFilter: Any?](./compositingfilter.md)
  A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [var backgroundFilters: [Any]?](./backgroundfilters.md)
  An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [var minificationFilter: CALayerContentsFilter](./minificationfilter.md)
  The filter used when reducing the size of the content.
- [var magnificationFilter: CALayerContentsFilter](./magnificationfilter.md)
  The filter used when increasing the size of the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/minificationfilterbias)*