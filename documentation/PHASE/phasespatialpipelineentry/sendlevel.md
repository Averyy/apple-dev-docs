# sendLevel

**Framework**: PHASE  
**Kind**: property

The amount of audio signal to add to the output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sendLevel: Double { get set }
```

#### Discussion

The framework clamps the value to the range between `0` and `1`, where `0` silences the audio and `1` passes the audio through to the output at full volume. The default value is `1`.

When an app adds the entry’s spatial pipeline (see [`entries`](phasespatialpipeline/entries.md)) to a sound event, the framework observes no further adjustments to this property. To change the send level after that, adjust the [`sendLevelMetaParameterDefinition`](phasespatialpipelineentry/sendlevelmetaparameterdefinition.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipelineentry/sendlevel)*