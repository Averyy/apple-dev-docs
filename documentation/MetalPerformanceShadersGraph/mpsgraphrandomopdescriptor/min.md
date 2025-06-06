# min

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The lower range of the distribution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var min: Float { get set }
```

#### Discussion

This value is used for Uniform distributions with float data types and Truncated Normal disributions. Defaults to 0 for uniform distributions and -2 for normal distributions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomopdescriptor/min)*