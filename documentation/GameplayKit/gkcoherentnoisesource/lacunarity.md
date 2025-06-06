# lacunarity

**Framework**: GameplayKit  
**Kind**: property

The rate at which successive octaves of the noise function increase in frequency.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var lacunarity: Double { get set }
```

#### Discussion

Coherent noise is composed from several applications of a pseudorandom function. Each successive application, or , increases in frequency and decreases in amplitude relative to the previous octave. This combination of many octaves produces the fractal appearance that makes coherent noise resemble natural phenomena like clouds, stone, and water.

Lacunarity determines the change in frequency between octaves. Smaller values result in coarser noise with more visible structure; finer values result in finer, more uniform noise. The default value is `2.0`.

## See Also

- [var frequency: Double](gkcoherentnoisesource/frequency.md)
  A value that determines the size and spacing of features in generated noise.
- [var octaveCount: Int](gkcoherentnoisesource/octavecount.md)
  The number of octaves of the underlying noise function to use for generating noise.
- [var seed: Int32](gkcoherentnoisesource/seed.md)
  The value that determines the specific configuration of noise produced by the noise source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource/lacunarity)*