# inputImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The image to use as an input image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * inputImage;
```

## See Also

### Instance Properties
- [var colorSpace: CGColorSpace?](./colorspace.md)
  The working color space.
- [var curvesData: Data](./curvesdata.md)
  Color values that determine the color curves transform.
- [var curvesDomain: CIVector](./curvesdomain.md)
  A two-element vector that defines the minimum and maximum values of the curve data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcurves/inputimage)*