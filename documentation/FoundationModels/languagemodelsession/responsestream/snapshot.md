# LanguageModelSession.ResponseStream.Snapshot

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A snapshot of partially generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct Snapshot
```

Available when `Content` conforms to `Generable`.

## Topics

### Inspecting a snapshot
- [var content: Content.PartiallyGenerated](./snapshot/content.md)
  The content of the response.
- [var rawContent: GeneratedContent](./snapshot/rawcontent.md)
  The raw content of the response.
- [var transcriptEntries: ArraySlice<Transcript.Entry>](./snapshot/transcriptentries.md)
  The list of transcript entries.
### Inspecting the token usage
- [var usage: LanguageModelSession.Usage](./snapshot/usage.md)
  Information about how many tokens were used by this response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/snapshot)*