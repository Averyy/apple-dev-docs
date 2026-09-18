# LanguageModelExecutorGenerationChannel.DataEntry

**Framework**: Foundation Models  
**Kind**: struct

A top-level data-entry event addressed to a transcript entry.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
struct DataEntry
```

#### Overview

A [`LanguageModelExecutorGenerationChannel.DataEntry`](languagemodelexecutorgenerationchannel/dataentry.md) event carries an entry-level action; the currently defined action is [`update(contentType:content:metadata:)`](languagemodelexecutorgenerationchannel/dataentry/action-swift.struct/update(contenttype:content:metadata:).md), which upserts a data entry with the given fields — replacing the existing entry that matches `entryID`, or appending a new one.

## Topics

### Structures
- [LanguageModelExecutorGenerationChannel.DataEntry.Action](languagemodelexecutorgenerationchannel/dataentry/action-swift.struct.md)
  An operation that can be performed on a data entry.
- [LanguageModelExecutorGenerationChannel.DataEntry.Update](languagemodelexecutorgenerationchannel/dataentry/update.md)
  The content carried by an [`update(contentType:content:metadata:)`](languagemodelexecutorgenerationchannel/dataentry/action-swift.struct/update(contenttype:content:metadata:).md) action.
### Instance Properties
- [var action: LanguageModelExecutorGenerationChannel.DataEntry.Action](languagemodelexecutorgenerationchannel/dataentry/action-swift.property.md)
  The action to perform.
- [var entryID: String?](languagemodelexecutorgenerationchannel/dataentry/entryid.md)
  The identifier for the entry.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/dataentry)*