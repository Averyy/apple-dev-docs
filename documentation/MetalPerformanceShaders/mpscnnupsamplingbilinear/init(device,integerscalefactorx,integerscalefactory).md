# init(device:integerScaleFactorX:integerScaleFactorY:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a bilinear spatial upsampling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice, integerScaleFactorX: Int, integerScaleFactorY: Int)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device integerScaleFactorX:(NSUInteger) integerScaleFactorX integerScaleFactorY:(NSUInteger) integerScaleFactorY;
```

## See Also

### Initializers
- [init(device: any MTLDevice, integerScaleFactorX: Int, integerScaleFactorY: Int, alignCorners: Bool)](./init%28device,integerscalefactorx,integerscalefactory,aligncorners%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingbilinear/init(device:integerscalefactorx:integerscalefactory:))*