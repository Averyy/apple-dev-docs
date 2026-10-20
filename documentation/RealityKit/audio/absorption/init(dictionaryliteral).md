# init(dictionaryLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates an absorption data set from a sequence of pairs of center frequency and Sabine absorption coefficient.

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

The Sabine absorption coefficient is a value between zero and one that describes the proportion of incident sound energy a surface absorbs.

The values will be interpolated and/or extrapolated to cover the audible frequency range.

```None
let data: Audio.Absorption = [500: 0.3, 1000: 0.4, 4000: 0.5]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/absorption/init(dictionaryliteral:))*