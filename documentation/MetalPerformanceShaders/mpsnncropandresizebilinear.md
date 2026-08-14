# MPSNNCropAndResizeBilinear

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnncropandresizebilinear/init(coder:device:).md)
- [init(device: any MTLDevice, resizeWidth: Int, resizeHeight: Int, numberOfRegions: Int, regions: UnsafePointer<MPSRegion>)](mpsnncropandresizebilinear/init(device:resizewidth:resizeheight:numberofregions:regions:).md)
### Instance Properties
- [var numberOfRegions: Int](mpsnncropandresizebilinear/numberofregions.md)
- [var regions: UnsafePointer<MPSRegion>](mpsnncropandresizebilinear/regions.md)
- [var resizeHeight: Int](mpsnncropandresizebilinear/resizeheight.md)
- [var resizeWidth: Int](mpsnncropandresizebilinear/resizewidth.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncropandresizebilinear)*