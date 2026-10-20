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
- [var aspectRatio: Float](./aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var parameterB: Float](./parameterb.md)
  The value of B to use for the cubic resampling function.
- [var parameterC: Float](./parameterc.md)
  The value of C to use for the cubic resampling function.
- [var scale: Float](./scale.md)
  The scaling factor to use on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibicubicscaletransform/inputimage)*