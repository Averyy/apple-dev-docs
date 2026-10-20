# sharpness

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The sharpness of the final image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var sharpness: Float { get set }
```

```objc
@property (nonatomic) float sharpness;
```

#### Discussion

The larger the value, the sharper the result.

## See Also

### Instance Properties
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var noiseLevel: Float](./noiselevel.md)
  The amount of noise reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cinoisereduction/sharpness)*