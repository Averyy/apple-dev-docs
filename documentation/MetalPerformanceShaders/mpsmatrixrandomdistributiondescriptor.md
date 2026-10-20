# MPSMatrixRandomDistributionDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSMatrixRandomDistributionDescriptor : NSObject
```

## Topics

### Instance Properties
- [var distributionType: MPSMatrixRandomDistribution](./mpsmatrixrandomdistributiondescriptor/distributiontype.md)
- [var maximum: Float](./mpsmatrixrandomdistributiondescriptor/maximum.md)
- [var mean: Float](./mpsmatrixrandomdistributiondescriptor/mean.md)
- [var minimum: Float](./mpsmatrixrandomdistributiondescriptor/minimum.md)
- [var standardDeviation: Float](./mpsmatrixrandomdistributiondescriptor/standarddeviation.md)
### Type Methods
- [class func `default`() -> MPSMatrixRandomDistributionDescriptor](./mpsmatrixrandomdistributiondescriptor/default%28%29.md)
- [class func normalDistributionDescriptor(withMean: Float, standardDeviation: Float) -> MPSMatrixRandomDistributionDescriptor](./mpsmatrixrandomdistributiondescriptor/normaldistributiondescriptor%28withmean,standarddeviation%29.md)
- [class func normalDistributionDescriptor(withMean: Float, standardDeviation: Float, minimum: Float, maximum: Float) -> MPSMatrixRandomDistributionDescriptor](./mpsmatrixrandomdistributiondescriptor/normaldistributiondescriptor%28withmean,standarddeviation,minimum,maximum%29.md)
- [class func uniformDistributionDescriptor(withMinimum: Float, maximum: Float) -> MPSMatrixRandomDistributionDescriptor](./mpsmatrixrandomdistributiondescriptor/uniformdistributiondescriptor%28withminimum,maximum%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandomdistributiondescriptor)*