# LanguageModelSession.ResponseStream.Snapshot

**Framework**: Foundation Models  
**Kind**: struct

A snapshot of partially generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Snapshot
```

## Topics

### Inspecting a snapshot
- [var content: Content.PartiallyGenerated](languagemodelsession/responsestream/snapshot/content.md)
  The content of the response.
- [var rawContent: GeneratedContent](languagemodelsession/responsestream/snapshot/rawcontent.md)
  The raw content of the response.
- [var transcriptEntries: ArraySlice<Transcript.Entry>](languagemodelsession/responsestream/snapshot/transcriptentries.md)
  The list of transcript entries.
### Inspecting the token usage
- [var usage: LanguageModelSession.Usage](languagemodelsession/responsestream/snapshot/usage.md)
  Information about how many tokens were used by this response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/snapshot)*