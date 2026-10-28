# rate

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A playback speed for the node’s audio.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var rate: Double { get set }
```

```objc
@property (nonatomic, assign) double rate;
```

## Discussion

The value clamps to the range `[0.25,` `4]`. The default value is `1`, which doesn’t change the source audio’s rate. Values higher than `1` speed up playback, and lower values slow it down.

## See Also

### Controlling Audio Playback
- [var rateMetaParameterDefinition: PHASENumberMetaParameterDefinition?](./ratemetaparameterdefinition.md)
  A meta parameter that dynamically changes the audio’s rate.
- [var gainMetaParameterDefinition: PHASENumberMetaParameterDefinition?](./gainmetaparameterdefinition.md)
  A meta parameter that dynamically changes the audio’s loudness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeneratornodedefinition/rate)*