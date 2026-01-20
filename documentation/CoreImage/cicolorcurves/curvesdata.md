# curvesData

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

Color values that determine the color curves transform.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var curvesData: Data { get set }
```

#### Discussion

Create the curves data as an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing a sequence of single-precision RGB values. These values represent a lookup table that’s applied to the input image.

Core Image unpremultiplies the image before applying the effect, and premultiplies the result after applying the effect.

## See Also

- [var colorSpace: CGColorSpace?](cicolorcurves/colorspace.md)
  The working color space.
- [var curvesDomain: CIVector](cicolorcurves/curvesdomain.md)
  A two-element vector that defines the minimum and maximum values of the curve data.
- [var inputImage: CIImage?](cicolorcurves/inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcurves/curvesdata)*