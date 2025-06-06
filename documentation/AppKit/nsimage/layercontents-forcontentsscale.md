# layerContents(forContentsScale:)

**Framework**: AppKit  
**Kind**: method

Returns an object that may be used as the contents of a layer.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func layerContents(forContentsScale layerContentsScale: CGFloat) -> Any
```

#### Return Value

A object that you can assign to the [`contents`](https://developer.apple.com/documentation/QuartzCore/CALayer/contents) property of a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) object. This object contains the image data from the current image optimized for the specified scale factor.

#### Discussion

Use this method in situations where you want to use the image as the contents of a layer. This method provides the image data wrapped in an object that correctly respects all of the possible content gravities supported by the layer. Use of the returned object as the layer’s contents is recommended over the use of the `NSImage` object itself.

## Parameters

- `layerContentsScale`: The scale factor for the resulting image. Obtain the value for this parameter by calling the   method.

## See Also

- [func recommendedLayerContentsScale(CGFloat) -> CGFloat](nsimage/recommendedlayercontentsscale(_:).md)
  Returns the recommended layer contents scale for this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/layercontents(forcontentsscale:))*