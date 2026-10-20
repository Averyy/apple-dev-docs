# sfntDirectoryEntry

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
struct sfntDirectoryEntry
```

```c
struct sfntDirectoryEntry;
```

## Topics

### Initializers
- [init()](./sfntdirectoryentry/init%28%29.md)
- [init(tableTag: FourCharCode, checkSum: UInt32, offset: UInt32, length: UInt32)](./sfntdirectoryentry/init%28tabletag,checksum,offset,length%29.md)
### Instance Properties
- [var checkSum: UInt32](./sfntdirectoryentry/checksum.md)
- [var length: UInt32](./sfntdirectoryentry/length.md)
- [var offset: UInt32](./sfntdirectoryentry/offset.md)
- [var tableTag: FourCharCode](./sfntdirectoryentry/tabletag.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/sfntdirectoryentry)*