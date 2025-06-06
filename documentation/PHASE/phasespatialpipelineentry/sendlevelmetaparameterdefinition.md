# sendLevelMetaParameterDefinition

**Framework**: PHASE  
**Kind**: property

A parameter that gradually updates the amount of audio signal that passes through to the output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sendLevelMetaParameterDefinition: PHASENumberMetaParameterDefinition? { get set }
```

#### Discussion

Use this property to fade reverb effects into a spatial mixer’s output.

For example, to begin with no reverb and gradually enable it, start by silencing reverb by setting the [`lateReverb`](phasespatialcategory/latereverb.md) entry’s [`sendLevel`](phasespatialpipelineentry/sendlevel.md) to `0`. Begin the fade by calling [`fade(value:duration:)`](phasenumbermetaparameter/fade(value:duration:).md) on this property with an argument of `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipelineentry/sendlevelmetaparameterdefinition)*