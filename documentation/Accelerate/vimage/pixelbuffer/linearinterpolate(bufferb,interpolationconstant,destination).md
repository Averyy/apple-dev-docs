# linearInterpolate(bufferB:interpolationConstant:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func linearInterpolate(bufferB: vImage.PixelBuffer<Format>, interpolationConstant: Float, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` conforms to `StaticPixelFormat` and `Format.ComponentType` is `Float`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/linearinterpolate(bufferb:interpolationconstant:destination:))*