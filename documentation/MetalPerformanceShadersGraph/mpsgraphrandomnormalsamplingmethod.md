# MPSGraphRandomNormalSamplingMethod

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The sampling method to use when generating values in the normal distribution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphRandomNormalSamplingMethod
```

## Topics

### Enumeration Cases
- [MPSGraphRandomNormalSamplingMethod.boxMuller](mpsgraphrandomnormalsamplingmethod/boxmuller.md)
  Use Box Muller transform to convert uniform values to values in the normal distribution. For bounded distributions this is a rejection sampling method.
- [MPSGraphRandomNormalSamplingMethod.invCDF](mpsgraphrandomnormalsamplingmethod/invcdf.md)
  Use inverse erf to convert uniform values to values in the normal distribution
### Initializers
- [init?(rawValue: UInt64)](mpsgraphrandomnormalsamplingmethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomnormalsamplingmethod)*