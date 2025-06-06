# scalingMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scaling mode of the fast fourier transform (FFT) operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var scalingMode: MPSGraphFFTScalingMode { get set }
```

#### Discussion

Note that the scaling mode is independent from the phase factor. Default value: `MPSGraphFFTScalingModeNone`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftdescriptor/scalingmode)*