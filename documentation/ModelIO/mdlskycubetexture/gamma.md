# gamma

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The amount of gamma correction to apply during tone mapping.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var gamma: Float { get set }
```

```objc
@property (nonatomic, assign) float gamma;
```

## Discussion

To render a sky texture, Model I/O first simulates the colors visible in the sky at different directions and then applies tone mapping to fit the resulting colors into the range of displayable values. As part of this process, Model I/O applies this property to the gamma curve of the texture image.

## See Also

### Working with Tone Mapping Parameters
- [var exposure: Float](./exposure.md)
  The amount of exposure compensation to apply during tone mapping.
- [var brightness: Float](./brightness.md)
  The amount of brightness enhancement to apply during tone mapping.
- [var contrast: Float](./contrast.md)
  The amount of contrast enhancement to apply during tone mapping.
- [var saturation: Float](./saturation.md)
  The amount of saturation enhancement to apply during tone mapping.
- [var highDynamicRangeCompression: vector_float2](./highdynamicrangecompression.md)
  Two parameters that determine the brightness compression curve for colors in the texture image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/gamma)*