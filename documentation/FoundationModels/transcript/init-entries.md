# init(entries:)

**Framework**: Foundation Models  
**Kind**: init

Creates a transcript.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(entries: some Sequence<Transcript.Entry> = [])
```

## Parameters

- `entries`: An array of entries to seed the transcript.

## See Also

- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.
- [Transcript.Segment](transcript/segment.md)
  The types of segments that may be included in a transcript entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/init(entries:))*