# init(bookmarkName:atByteSampleOffset:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithBookmarkName:(NSString *) mark atByteSampleOffset:(NSInteger) byteSampleOffset;
```

## Parameters

- `mark`: The name of the bookmark.
- `byteSampleOffset`: The byte offset into the audio buffer.

## See Also

### Creating a marker
- [init(markerType: AVSpeechSynthesisMarker.Mark, forTextRange: NSRange, atByteSampleOffset: Int)](./init%28markertype,fortextrange,atbytesampleoffset%29.md)
  Creates a marker with a type and location of the request’s text.
- [init(wordRange: NSRange, atByteSampleOffset: Int)](./init%28wordrange,atbytesampleoffset%29.md)
  Creates a word marker with a range of the word and offset into the audio buffer.
- [init(sentenceRange: NSRange, atByteSampleOffset: Int)](./init%28sentencerange,atbytesampleoffset%29.md)
  Creates a sentence marker with a range of the sentence and offset into the audio buffer.
- [init(paragraphRange: NSRange, atByteSampleOffset: Int)](./init%28paragraphrange,atbytesampleoffset%29.md)
  Creates a paragraph marker with a range of the paragraph and offset into the audio buffer.
- [init(phonemeString: String, atByteSampleOffset: Int)](./init%28phonemestring,atbytesampleoffset%29.md)
  Creates a phoneme marker with a range of the phoneme and offset into the audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker/init(bookmarkname:atbytesampleoffset:))*