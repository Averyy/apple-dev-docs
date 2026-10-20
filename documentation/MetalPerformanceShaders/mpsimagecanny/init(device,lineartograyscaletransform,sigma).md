# init(device:linearToGrayScaleTransform:sigma:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, linearToGrayScaleTransform transform: UnsafePointer<Float>, sigma: Float)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device linearToGrayScaleTransform:(const float *) transform sigma:(const float) sigma;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecanny/init(device:lineartograyscaletransform:sigma:))*