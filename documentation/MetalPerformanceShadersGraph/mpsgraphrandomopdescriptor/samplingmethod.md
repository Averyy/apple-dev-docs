# samplingMethod

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The sampling method of the distribution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var samplingMethod: MPSGraphRandomNormalSamplingMethod { get set }
```

#### Discussion

This value is used for Normal and Truncated Normal disributions. See MPSGraphRandomNormalSamplingMethod. Defaults to MPSGraphRandomNormalSamplingInvCDF.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomopdescriptor/samplingmethod)*