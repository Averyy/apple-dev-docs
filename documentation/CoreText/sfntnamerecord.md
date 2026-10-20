# sfntNameRecord

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
struct sfntNameRecord
```

```c
struct sfntNameRecord;
```

## Topics

### Initializers
- [init()](./sfntnamerecord/init%28%29.md)
- [init(platformID: UInt16, scriptID: UInt16, languageID: UInt16, nameID: UInt16, length: UInt16, offset: UInt16)](./sfntnamerecord/init%28platformid,scriptid,languageid,nameid,length,offset%29.md)
### Instance Properties
- [var languageID: UInt16](./sfntnamerecord/languageid.md)
- [var length: UInt16](./sfntnamerecord/length.md)
- [var nameID: UInt16](./sfntnamerecord/nameid.md)
- [var offset: UInt16](./sfntnamerecord/offset.md)
- [var platformID: UInt16](./sfntnamerecord/platformid.md)
- [var scriptID: UInt16](./sfntnamerecord/scriptid.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/sfntnamerecord)*