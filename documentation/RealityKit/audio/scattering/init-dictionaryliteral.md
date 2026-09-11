# init(dictionaryLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a scattering data set from a sequence of pairs of center frequency and scattering coefficient.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(dictionaryLiteral elements: (Float, Float)...)
```

#### Discussion

The scattering coefficient is a value between zero and one that describes the proportion of incident sound energy that is diffused or redirected by a surface, rather than absorbed.

The values will be interpolated and/or extrapolated to cover the audible frequency range.

```None
let data: Audio.Scattering = [500: 0.3, 1000: 0.4, 4000: 0.5]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/scattering/init(dictionaryliteral:))*