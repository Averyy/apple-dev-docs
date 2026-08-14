# MPSMatrixRandomDistributionDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixRandomDistributionDescriptor
```

## Topics

### Instance Properties
- [var distributionType: MPSMatrixRandomDistribution](mpsmatrixrandomdistributiondescriptor/distributiontype.md)
- [var maximum: Float](mpsmatrixrandomdistributiondescriptor/maximum.md)
- [var mean: Float](mpsmatrixrandomdistributiondescriptor/mean.md)
- [var minimum: Float](mpsmatrixrandomdistributiondescriptor/minimum.md)
- [var standardDeviation: Float](mpsmatrixrandomdistributiondescriptor/standarddeviation.md)
### Type Methods
- [class func `default`() -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/default.md)
- [class func normalDistributionDescriptor(withMean: Float, standardDeviation: Float) -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/normaldistributiondescriptor(withmean:standarddeviation:).md)
- [class func normalDistributionDescriptor(withMean: Float, standardDeviation: Float, minimum: Float, maximum: Float) -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/normaldistributiondescriptor(withmean:standarddeviation:minimum:maximum:).md)
- [class func uniformDistributionDescriptor(withMinimum: Float, maximum: Float) -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/uniformdistributiondescriptor(withminimum:maximum:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandomdistributiondescriptor)*