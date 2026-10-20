# sfntFeatureHeader

**Framework**: Core Text  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct sfntFeatureHeader
```

```c
struct sfntFeatureHeader;
```

## Topics

### Initializers
- [init()](./sfntfeatureheader/init%28%29.md)
- [init(version: Int32, featureNameCount: UInt16, featureSetCount: UInt16, reserved: Int32, names: sfntFeatureName, settings: sfntFontFeatureSetting, runs: sfntFontRunFeature)](./sfntfeatureheader/init%28version,featurenamecount,featuresetcount,reserved,names,settings,runs%29.md)
### Instance Properties
- [var featureNameCount: UInt16](./sfntfeatureheader/featurenamecount.md)
- [var featureSetCount: UInt16](./sfntfeatureheader/featuresetcount.md)
- [var names: sfntFeatureName](./sfntfeatureheader/names.md)
- [var reserved: Int32](./sfntfeatureheader/reserved.md)
- [var runs: sfntFontRunFeature](./sfntfeatureheader/runs.md)
- [var settings: sfntFontFeatureSetting](./sfntfeatureheader/settings.md)
- [var version: Int32](./sfntfeatureheader/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structures
- [struct AnchorPoint](./anchorpoint.md)
- [struct AnchorPointTable](./anchorpointtable.md)
- [struct AnkrTable](./ankrtable.md)
- [struct BslnFormat0Part](./bslnformat0part.md)
- [struct BslnFormat1Part](./bslnformat1part.md)
- [struct BslnFormat2Part](./bslnformat2part.md)
- [struct BslnFormat3Part](./bslnformat3part.md)
- [struct BslnFormatUnion](./bslnformatunion.md)
- [struct BslnTable](./bslntable.md)
- [struct FontVariation](./fontvariation.md)
- [struct JustDirectionTable](./justdirectiontable.md)
- [struct JustPCAction](./justpcaction.md)
- [struct JustPCActionSubrecord](./justpcactionsubrecord.md)
- [struct JustPCConditionalAddAction](./justpcconditionaladdaction.md)
- [struct JustPCDecompositionAction](./justpcdecompositionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/sfntfeatureheader)*