# MPSImageCanny

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagecanny/init(coder:device:).md)
- [convenience init(device: any MTLDevice)](mpsimagecanny/init(device:).md)
- [init(device: any MTLDevice, linearToGrayScaleTransform: UnsafePointer<Float>, sigma: Float)](mpsimagecanny/init(device:lineartograyscaletransform:sigma:).md)
### Instance Properties
- [var colorTransform: UnsafePointer<Float>](mpsimagecanny/colortransform.md)
- [var highThreshold: Float](mpsimagecanny/highthreshold.md)
- [var lowThreshold: Float](mpsimagecanny/lowthreshold.md)
- [var sigma: Float](mpsimagecanny/sigma.md)
- [var useFastMode: Bool](mpsimagecanny/usefastmode.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecanny)*