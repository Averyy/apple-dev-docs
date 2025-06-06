# inverse

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A Boolean-valued parameter that defines the phase factor sign for Fourier transforms.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var inverse: Bool { get set }
```

#### Discussion

When set to `YES` graph uses the positive phase factor: `exp(+i 2Pi mu nu / n)`, when computing the (inverse) Fourier transform. Otherwise MPSGraph uses the negative phase factor: `exp(-i 2Pi mu nu / n)`, when computing the Fourier transform. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftdescriptor/inverse)*