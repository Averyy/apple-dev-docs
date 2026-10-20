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
- [var point0: CGPoint](./point0.md)
  The first point in the focused region of the output image.
- [var point1: CGPoint](./point1.md)
  The second point in the focused region of the output image.
- [var radius: Float](./radius.md)
  The distance from the center of the effect.
- [var saturation: Float](./saturation.md)
  The amount to adjust the saturation by.
- [var unsharpMaskIntensity: Float](./unsharpmaskintensity.md)
  The intensity of the unsharp mask effect applied to the in-focus area.
- [var unsharpMaskRadius: Float](./unsharpmaskradius.md)
  The radius of the unsharp mask effect applied to the in-focus area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidepthoffield/inputimage)*