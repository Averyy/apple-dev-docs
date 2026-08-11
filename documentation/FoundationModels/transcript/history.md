# history

**Framework**: Foundation Models  
**Kind**: property

The transcript entries excluding the leading instructions entry, if present.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var history: Transcript.HistoryView { get set }
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)

#### Discussion

Use `history` to access just the conversational entries — prompts, responses, tool calls, and tool outputs — without the initial instructions that were used to configure the session.

When reading, if the first entry in the transcript is an [`Transcript.Entry.instructions(_:)`](transcript/entry/instructions(_:).md) entry, it is excluded from the returned view. All other entries, including any subsequent instructions entries, are included.

When writing, the new value replaces all entries except the leading instructions entry, which is preserved.

## See Also

- [Transcript.HistoryView](transcript/historyview.md)
  A mutable view into the conversational entries of a [`Transcript`](transcript.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/history)*