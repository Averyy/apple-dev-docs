# STHeader

**Framework**: Core Text  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct STHeader
```

## Topics

### Initializers
- [init()](stheader/init.md)
- [init(filler: UInt8, nClasses: STClass, classTableOffset: UInt16, stateArrayOffset: UInt16, entryTableOffset: UInt16)](stheader/init(filler:nclasses:classtableoffset:statearrayoffset:entrytableoffset:).md)
### Instance Properties
- [var classTableOffset: UInt16](stheader/classtableoffset.md)
- [var entryTableOffset: UInt16](stheader/entrytableoffset.md)
- [var filler: UInt8](stheader/filler.md)
- [var nClasses: STClass](stheader/nclasses.md)
- [var stateArrayOffset: UInt16](stheader/statearrayoffset.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AnchorPoint](anchorpoint.md)
- [struct AnchorPointTable](anchorpointtable.md)
- [struct AnkrTable](ankrtable.md)
- [struct BslnFormat0Part](bslnformat0part.md)
- [struct BslnFormat1Part](bslnformat1part.md)
- [struct BslnFormat2Part](bslnformat2part.md)
- [struct BslnFormat3Part](bslnformat3part.md)
- [struct BslnFormatUnion](bslnformatunion.md)
- [struct BslnTable](bslntable.md)
- [struct FontVariation](fontvariation.md)
- [struct JustDirectionTable](justdirectiontable.md)
- [struct JustPCAction](justpcaction.md)
- [struct JustPCActionSubrecord](justpcactionsubrecord.md)
- [struct JustPCConditionalAddAction](justpcconditionaladdaction.md)
- [struct JustPCDecompositionAction](justpcdecompositionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/stheader)*