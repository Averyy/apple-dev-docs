# LanguageModelExecutorGenerationChannel.DataEntry

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A top-level data-entry event addressed to a transcript entry.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct DataEntry
```

#### Overview

A [`LanguageModelExecutorGenerationChannel.DataEntry`](./dataentry.md) event carries an entry-level action; the currently defined action is [`update(contentType:content:metadata:)`](./dataentry/action-swift.struct/update%28contenttype,content,metadata%29.md), which upserts a data entry with the given fields — replacing the existing entry that matches `entryID`, or appending a new one.

## Topics

### Structures
- [LanguageModelExecutorGenerationChannel.DataEntry.Action](./dataentry/action-swift.struct.md)
  An operation that can be performed on a data entry.
- [LanguageModelExecutorGenerationChannel.DataEntry.Update](./dataentry/update.md)
  The content carried by an [`update(contentType:content:metadata:)`](./dataentry/action-swift.struct/update%28contenttype,content,metadata%29.md) action.
### Instance Properties
- [var action: LanguageModelExecutorGenerationChannel.DataEntry.Action](./dataentry/action-swift.property.md)
  The action to perform.
- [var entryID: String?](./dataentry/entryid.md)
  The identifier for the entry.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/dataentry)*