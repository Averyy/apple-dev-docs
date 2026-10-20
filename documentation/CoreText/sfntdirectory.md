# sfntDirectory

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
struct sfntDirectory
```

```c
struct sfntDirectory;
```

## Topics

### Initializers
- [init()](./sfntdirectory/init%28%29.md)
- [init(format: FourCharCode, numOffsets: UInt16, searchRange: UInt16, entrySelector: UInt16, rangeShift: UInt16, table: sfntDirectoryEntry)](./sfntdirectory/init%28format,numoffsets,searchrange,entryselector,rangeshift,table%29.md)
### Instance Properties
- [var entrySelector: UInt16](./sfntdirectory/entryselector.md)
- [var format: FourCharCode](./sfntdirectory/format.md)
- [var numOffsets: UInt16](./sfntdirectory/numoffsets.md)
- [var rangeShift: UInt16](./sfntdirectory/rangeshift.md)
- [var searchRange: UInt16](./sfntdirectory/searchrange.md)
- [var table: sfntDirectoryEntry](./sfntdirectory/table.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/sfntdirectory)*