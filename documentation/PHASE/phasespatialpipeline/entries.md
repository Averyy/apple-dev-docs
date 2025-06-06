# entries

**Framework**: PHASE  
**Kind**: property

Audio layers for environmental effects to add to the output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var entries: [PHASESpatialCategory : PHASESpatialPipelineEntry] { get }
```

#### Discussion

This property includes an entry for each spatial category that the app includes in the [`init(flags:)`](phasespatialpipeline/init(flags:).md) argument. Adjust an entry’s send level to blend its audio layer into the output signal. For example, by fading the input audio signal using the [`sendLevelMetaParameterDefinition`](phasespatialpipelineentry/sendlevelmetaparameterdefinition.md) property of the [`directPathTransmission`](phasespatialpipeline/flags-swift.struct/directpathtransmission.md) entry, the app can lower the dry signal and blend in the right balance of early reflections and reverb.

## See Also

- [var flags: PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.property.md)
  A collection of environmental effects to include in the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipeline/entries)*