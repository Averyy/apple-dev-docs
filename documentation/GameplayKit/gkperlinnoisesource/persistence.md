# persistence

**Framework**: GameplayKit  
**Kind**: property

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

#### Discussion

Coherent noise is composed from several applications of a pseudorandom function. Each successive application, or , increases in frequency and decreases in amplitude relative to the previous octave. This combination of many octaves produces the fractal appearance that makes coherent noise resemble natural phenomena like clouds, stone, and water.

Persistence determines the change in amplitude between octaves. Smaller values result in smoother noise; larger values increase roughness. The default value is `0.5`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkperlinnoisesource/persistence)*