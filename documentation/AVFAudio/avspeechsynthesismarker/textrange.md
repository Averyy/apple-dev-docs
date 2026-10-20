# textRange

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The location and length of the request’s text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var textRange: NSRange { get set }
```

```objc
@property (nonatomic, assign) NSRange textRange;
```

## See Also

### Inspecting a marker
- [var mark: AVSpeechSynthesisMarker.Mark](./mark-swift.property.md)
  The type that describes the text.
- [var bookmarkName: String](./bookmarkname.md)
  A string that represents the name of a bookmark.
- [var phoneme: String](./phoneme.md)
  A string that represents a distinct sound.
- [var byteSampleOffset: Int](./bytesampleoffset.md)
  The byte offset into the audio buffer.
- [AVSpeechSynthesisMarker.Mark](./mark-swift.enum.md)
  Constants that describe the type of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker/textrange)*