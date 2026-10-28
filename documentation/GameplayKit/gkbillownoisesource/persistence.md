# persistence

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The rate at which successive octaves of the noise function decrease in amplitude.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var persistence: Double { get set }
```

```objc
@property (nonatomic) double persistence;
```

## Discussion

Coherent noise is composed from several applications of a pseudorandom function. Each successive application, or *octave*, increases in frequency and decreases in amplitude relative to the previous octave. This combination of many octaves produces the fractal appearance that makes coherent noise resemble natural phenomena like clouds, stone, and water.

Persistence determines the change in amplitude between octaves. Smaller values result in smoother noise; larger values increase roughness. The default value is `0.5`.

## See Also

### Creating a Noise Source
- [init(frequency: Double, octaveCount: Int, persistence: Double, lacunarity: Double, seed: Int32)](./init%28frequency,octavecount,persistence,lacunarity,seed%29.md)
  Creates a billow noise source with the specified parameters.
- [+ billowNoiseSourceWithFrequency:octaveCount:persistence:lacunarity:seed:](./billownoisesourcewithfrequency_octavecount_persistence_lacunarity_seed_.md)
  Initializes a billow noise source with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource/persistence)*