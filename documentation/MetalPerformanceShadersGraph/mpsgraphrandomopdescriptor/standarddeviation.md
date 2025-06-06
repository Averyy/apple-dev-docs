# standardDeviation

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The standard deviation of the distribution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var standardDeviation: Float { get set }
```

#### Discussion

This value is used for Normal and Truncated Normal disributions. For Truncated Normal distribution this defines the standard deviation parameter of the underlying Normal distribution, that is the width of the Gaussian, not the true standard deviation of the truncated distribution which typically differs from the standard deviation of the original Normal distribution. Defaults to 0 for uniform distributions and 1 for normal distributions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomopdescriptor/standarddeviation)*