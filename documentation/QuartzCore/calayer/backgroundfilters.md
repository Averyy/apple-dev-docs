# backgroundFilters

**Framework**: Core Animation  
**Kind**: property

An array of Core Image filters to apply to the content immediately behind the layer. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var backgroundFilters: [Any]? { get set }
```

#### Discussion

Background filters affect the content behind the layer that shows through into the layer itself. Typically this content belongs to the superlayer that acts as the parent of the layer. These filters do not affect the content of the layer itself, including the layer’s background color and border.

The default value of this property is `nil`.

Changing the inputs of the [`CIFilter`](https://developer.apple.com/documentation/CoreImage/CIFilter-swift.class) object directly after it is attached to the layer causes undefined behavior. In macOS, it is possible to modify filter parameters after attaching them to the layer but you must use the layer’s doc://com.apple.documentation/documentation/objectivec/nsobject/1418139-setvalue method to do so. In addition, you must assign a name to the filter so that you can identify it in the array. For example, to change the `inputRadius` parameter of the filter, you could use code similar to the following:

You use the layer’s [`masksToBounds`](calayer/maskstobounds.md) to control the extent of its background filter’s effect.

The following code shows how to create two overlapping text layers, `background` and `foreground`. A Gaussian blur filter is added to the foreground layer’s [`backgroundFilters`](calayer/backgroundfilters.md) array and its [`masksToBounds`](calayer/maskstobounds.md) is set to [`true`](https://developer.apple.com/documentation/swift/true):

```swift
view.layer = CALayer()
view.layerUsesCoreImageFilters = true
     
let background = CATextLayer()
background.string = "background"
background.backgroundColor = NSColor.red.cgColor
background.alignmentMode = kCAAlignmentCenter
background.fontSize = 96
background.frame = CGRect(x: 10, y: 10, width: 640, height: 160)
     
let foreground = CATextLayer()
foreground.string = "foreground"
foreground.backgroundColor = NSColor.blue.cgColor
foreground.alignmentMode = kCAAlignmentCenter
foreground.fontSize = 48
foreground.opacity = 0.5
foreground.frame = CGRect(x: 20, y: 20, width: 600, height: 60)
foreground.masksToBounds = true
     
if let blurFilter = CIFilter(name: "CIGaussianBlur",
                             withInputParameters: [kCIInputRadiusKey: 2]) {
    foreground.backgroundFilters = [blurFilter]
}
     
view.layer?.addSublayer(background)
background.addSublayer(foreground)
```

The following figure shows the result: the background layer is only blurred where it is overlapped by the foreground layer.

![Background filter effect with mask to bounds](https://docs-assets.developer.apple.com/published/872d1fd56b8940c30020c805f2515c87/media-2851423%402x.png)

However, if the foreground layer’s [`masksToBounds`](calayer/maskstobounds.md) is set to [`false`](https://developer.apple.com/documentation/swift/false), the entire background layer is blurred as illustrated in the following figure.

![Background filter effect without mask to bounds](https://docs-assets.developer.apple.com/published/1408d14df377140131d12a954aea8241/media-2851424%402x.png)

##### Special Considerations

This property is not supported on layers in iOS.

## See Also

- [var filters: [Any]?](calayer/filters.md)
  An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [var compositingFilter: Any?](calayer/compositingfilter.md)
  A CoreImage filter used to composite the layer and the content behind it. Animatable.
- [var minificationFilter: CALayerContentsFilter](calayer/minificationfilter.md)
  The filter used when reducing the size of the content.
- [var minificationFilterBias: Float](calayer/minificationfilterbias.md)
  The bias factor used by the minification filter to determine the levels of detail.
- [var magnificationFilter: CALayerContentsFilter](calayer/magnificationfilter.md)
  The filter used when increasing the size of the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/backgroundfilters)*