# data(entryID:action:)

**Framework**: Foundation Models  
**Kind**: method

A data-entry event addressed to a transcript entry.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
static func data(entryID: String? = nil, action: LanguageModelExecutorGenerationChannel.DataEntry.Action) -> LanguageModelExecutorGenerationChannel.Event
```

#### Discussion

The entry’s `contentType` (from [`update(contentType:content:metadata:)`](languagemodelexecutorgenerationchannel/dataentry/action-swift.struct/update(contenttype:content:metadata:).md)) is checked against [`supportsDataEntryType(_:)`](languagemodel/supportsdataentrytype(_:).md) before the entry is appended, and rejected entries surface as [`LanguageModelError.unsupportedTranscriptContent(_:)`](languagemodelerror/unsupportedtranscriptcontent(_:).md).

## Parameters

- `entryID`: The identifier for the data entry to upsert. Pass `nil` to have the framework assign a fresh id.
- `action`: The operation to perform on the data entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event/data(entryid:action:))*