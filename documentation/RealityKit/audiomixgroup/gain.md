# gain

**Framework**: RealityKit  
**Kind**: property

The overall level for all sounds of an audio mix group in relative decibels.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var gain: Audio.Decibel { get set }
```

#### Discussion

The gain is a value in the range `[-.infinity, .zero]`, where `-.infinity` is silent and `.zero` is nominal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiomixgroup/gain)*