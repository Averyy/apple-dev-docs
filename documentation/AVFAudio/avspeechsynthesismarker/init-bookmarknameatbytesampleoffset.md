# init(bookmarkName:atByteSampleOffset:)

**Framework**: AVFAudio  
**Kind**: init

Creates a bookmark marker with a name and offset into the audio buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(bookmarkName mark: String, atByteSampleOffset byteSampleOffset: Int)
```

## Parameters

- `mark`: The name of the bookmark.
- `byteSampleOffset`: The byte offset into the audio buffer.

## See Also

- [init(markerType: AVSpeechSynthesisMarker.Mark, forTextRange: NSRange, atByteSampleOffset: Int)](avspeechsynthesismarker/init(markertype:fortextrange:atbytesampleoffset:).md)
  Creates a marker with a type and location of the request’s text.
- [init(wordRange: NSRange, atByteSampleOffset: Int)](avspeechsynthesismarker/init(wordrange:atbytesampleoffset:).md)
  Creates a word marker with a range of the word and offset into the audio buffer.
- [init(sentenceRange: NSRange, atByteSampleOffset: Int)](avspeechsynthesismarker/init(sentencerange:atbytesampleoffset:).md)
  Creates a sentence marker with a range of the sentence and offset into the audio buffer.
- [init(paragraphRange: NSRange, atByteSampleOffset: Int)](avspeechsynthesismarker/init(paragraphrange:atbytesampleoffset:).md)
  Creates a paragraph marker with a range of the paragraph and offset into the audio buffer.
- [init(phonemeString: String, atByteSampleOffset: Int)](avspeechsynthesismarker/init(phonemestring:atbytesampleoffset:).md)
  Creates a phoneme marker with a range of the phoneme and offset into the audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker/init(bookmarkname:atbytesampleoffset:))*