# octaveCount

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The number of octaves of the underlying noise function to use for generating noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var octaveCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger octaveCount;
```

## Discussion

Coherent noise is composed from several applications of a pseudorandom function. Each successive application, or *octave*, increases in frequency and decreases in amplitude relative to the previous octave. This combination of many octaves produces the fractal appearance that makes coherent noise resemble natural phenomena like clouds, stone, and water.

This property determines the number of octaves of the noise function that the noise source combines to produce noise. A smaller number results in smoother, simpler output; larger numbers result in rougher, more complex output. The default value is `6`.

## See Also

### Managing Noise Generation Parameters
- [var frequency: Double](./frequency.md)
  A value that determines the size and spacing of features in generated noise.
- [var lacunarity: Double](./lacunarity.md)
  The rate at which successive octaves of the noise function increase in frequency.
- [var seed: Int32](./seed.md)
  The value that determines the specific configuration of noise produced by the noise source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource/octavecount)*