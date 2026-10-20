# MPSImageCanny

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageCanny
```

```objc
@interface MPSImageCanny : MPSUnaryImageKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimagecanny/init%28coder,device%29.md)
- [convenience init(device: any MTLDevice)](./mpsimagecanny/init%28device%29.md)
- [init(device: any MTLDevice, linearToGrayScaleTransform: UnsafePointer<Float>, sigma: Float)](./mpsimagecanny/init%28device,lineartograyscaletransform,sigma%29.md)
### Instance Properties
- [var colorTransform: UnsafePointer<Float>](./mpsimagecanny/colortransform.md)
- [var highThreshold: Float](./mpsimagecanny/highthreshold.md)
- [var lowThreshold: Float](./mpsimagecanny/lowthreshold.md)
- [var sigma: Float](./mpsimagecanny/sigma.md)
- [var useFastMode: Bool](./mpsimagecanny/usefastmode.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](./mpsunaryimagekernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecanny)*