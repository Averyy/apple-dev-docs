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
- [var radius: Float](./radius.md)
  The radius of the blur, in pixels.
- [var ringAmount: Float](./ringamount.md)
  The amount of extra emphasis at the ring of the bokeh.
- [var ringSize: Float](./ringsize.md)
  The radius of the extra emphasis at the ring of the bokeh.
- [var softness: Float](./softness.md)
  The softness of the bokeh effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibokehblur/inputimage)*