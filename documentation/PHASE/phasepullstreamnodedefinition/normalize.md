# normalize

**Framework**: PHASE  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var normalize: Bool { get set }
```

#### Discussion

In general, clients are advised to normalize the input. Normalization is required to properly calibrate the output level. If you set this value to NO, it’s advised that you do custom normalization of the audio data prior to passing the buffers to PHASE.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepullstreamnodedefinition/normalize)*