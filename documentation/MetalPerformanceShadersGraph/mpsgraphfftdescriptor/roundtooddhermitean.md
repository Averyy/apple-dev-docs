# roundToOddHermitean

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter which controls how graph rounds the output tensor size for a Hermitean-to-real Fourier transform.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var roundToOddHermitean: Bool { get set }
```

#### Discussion

If set to `YES` then MPSGraph rounds the last output dimension of the result tensor in [`HermiteanToRealFFT(_:axesTensor:descriptor:name:)`](mpsgraph/hermiteantorealfft(_:axestensor:descriptor:name:).md) to an odd value. Has no effect in the other Fourier transform operations. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftdescriptor/roundtooddhermitean)*