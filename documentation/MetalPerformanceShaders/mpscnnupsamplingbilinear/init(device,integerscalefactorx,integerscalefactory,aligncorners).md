# init(device:integerScaleFactorX:integerScaleFactorY:alignCorners:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, integerScaleFactorX: Int, integerScaleFactorY: Int, alignCorners: Bool)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device integerScaleFactorX:(NSUInteger) integerScaleFactorX integerScaleFactorY:(NSUInteger) integerScaleFactorY alignCorners:(BOOL) alignCorners;
```

## See Also

### Initializers
- [convenience init(device: any MTLDevice, integerScaleFactorX: Int, integerScaleFactorY: Int)](./init%28device,integerscalefactorx,integerscalefactory%29.md)
  Initializes a bilinear spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingbilinear/init(device:integerscalefactorx:integerscalefactory:aligncorners:))*