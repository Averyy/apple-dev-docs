# MPSNNCropAndResizeBilinear

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A cropping and bilinear resizing filter.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNCropAndResizeBilinear
```

```objc
@interface MPSNNCropAndResizeBilinear : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsnncropandresizebilinear/init%28coder,device%29.md)
- [init(device: any MTLDevice, resizeWidth: Int, resizeHeight: Int, numberOfRegions: Int, regions: UnsafePointer<MPSRegion>)](./mpsnncropandresizebilinear/init%28device,resizewidth,resizeheight,numberofregions,regions%29.md)
### Instance Properties
- [var numberOfRegions: Int](./mpsnncropandresizebilinear/numberofregions.md)
- [var regions: UnsafePointer<MPSRegion>](./mpsnncropandresizebilinear/regions.md)
- [var resizeHeight: Int](./mpsnncropandresizebilinear/resizeheight.md)
- [var resizeWidth: Int](./mpsnncropandresizebilinear/resizewidth.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncropandresizebilinear)*