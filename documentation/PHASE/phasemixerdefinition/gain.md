# gain

**Framework**: PHASE  
**Kind**: property

The mixer’s volume.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gain: Double { get set }
```

#### Discussion

This property modifies the volume of all the mixer’s audio in the output’s final stages. The framework clamps the value to the range between `0` and `1`, where `0` silences the audio and `1` doesn’t modify the audio’s original volume.

## See Also

- [var gainMetaParameterDefinition: PHASENumberMetaParameterDefinition?](phasemixerdefinition/gainmetaparameterdefinition.md)
  A template for a parameter that changes the mixer’s volume gradually over a period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixerdefinition/gain)*