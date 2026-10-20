# samplingLinear()

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Create an image by changing the receiver’s sample mode to bilinear interpolation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func samplingLinear() -> CIImage
```

```objc
- (CIImage *) imageBySamplingLinear;
```

#### Return Value

 An autoreleased [`CIImage`](../ciimage.md) instance with a bilinear sampling.

## See Also

### Sampling the Image
- [func samplingNearest() -> CIImage](./samplingnearest%28%29.md)
  Create an image by changing the receiver’s sample mode to nearest neighbor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/samplinglinear())*