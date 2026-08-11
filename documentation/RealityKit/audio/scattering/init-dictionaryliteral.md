# init(dictionaryLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a scattering data set from a sequence of pairs of center frequency and scattering coefficient.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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