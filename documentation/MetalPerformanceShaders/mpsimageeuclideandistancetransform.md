# MPSImageEuclideanDistanceTransform

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that performs a Euclidean distance transform on an image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSImageEuclideanDistanceTransform
```

## Topics

### Creating a Euclidean distance transform
- [init(device: any MTLDevice)](mpsimageeuclideandistancetransform/init(device:).md)
  Creates a Euclidean distance transform that runs on a specified device.
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageeuclideandistancetransform/init(coder:device:).md)
  Creates a Euclidean distance transform that uses a specified decoder for your data and runs on a specified device.
### Limiting the search for nonzero pixels
- [var searchLimitRadius: Float](mpsimageeuclideandistancetransform/searchlimitradius.md)
  Limits the search in an image from a pixel to the closest nonzero pixel within a specified radius.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageeuclideandistancetransform)*