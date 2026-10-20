# divide

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A blend kernel that divides the background image sample color with the foreground image sample color.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class var divide: CIBlendKernel { get }
```

```objc
@property (class, strong, readonly) CIBlendKernel * divide;
```

#### Discussion

![The result of using the divide blend kernel (background image is top left, foreground image is bottom left)](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-2926864@2x.png)

## See Also

### Builtin Blend Kernels
- [class var clear: CIBlendKernel](./clear.md)
  A blend kernel that returns a clear color.
- [class var color: CIBlendKernel](./color.md)
  A blend kernel that uses the luminance values of the background with the hue and saturation values of the foreground image.
- [class var colorBurn: CIBlendKernel](./colorburn.md)
  A blend kernel that darkens the background image samples to reflect the foreground image samples.
- [class var colorDodge: CIBlendKernel](./colordodge.md)
  A blend kernel that brightens the background image samples to reflect the foreground image samples.
- [class var componentAdd: CIBlendKernel](./componentadd.md)
  A blend kernel that adds color components to achieve a brightening effect.
- [class var componentMax: CIBlendKernel](./componentmax.md)
  A blend kernel that creates an image using the maximum values of two input images.
- [class var componentMin: CIBlendKernel](./componentmin.md)
  A blend kernel that creates an image using the minimum values of two input images.
- [class var componentMultiply: CIBlendKernel](./componentmultiply.md)
  A blend kernel that multiplies the color components of its input images.
- [class var darken: CIBlendKernel](./darken.md)
  A blend kernel that creates an image using the darker values of two input images.
- [class var darkerColor: CIBlendKernel](./darkercolor.md)
  A blend kernel that creates an image using the darker color of two input images.
- [class var destination: CIBlendKernel](./destination.md)
  A blend kernel that returns the background input image.
- [class var destinationAtop: CIBlendKernel](./destinationatop.md)
  A blend kernel that places the background over the foreground and crops based on the visibility of the foreground.
- [class var destinationIn: CIBlendKernel](./destinationin.md)
  A blend kernel that places the background over the foreground and crops based on the visibility of both.
- [class var destinationOut: CIBlendKernel](./destinationout.md)
  A blend kernel that uses the background image to define what to take out of the foreground image.
- [class var destinationOver: CIBlendKernel](./destinationover.md)
  A blend kernel that places the background image over the input foreground image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel/divide)*