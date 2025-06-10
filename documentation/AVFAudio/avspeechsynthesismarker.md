# AVSpeechSynthesisMarker

**Framework**: AVFAudio  
**Kind**: class

An object that contains information about the synthesized audio.

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
class AVSpeechSynthesisMarker
```

## Topics

### Creating a marker
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
- [init(bookmarkName: String, atByteSampleOffset: Int)](avspeechsynthesismarker/init(bookmarkname:atbytesampleoffset:).md)
  Creates a bookmark marker with a name and offset into the audio buffer.
### Inspecting a marker
- [var mark: AVSpeechSynthesisMarker.Mark](avspeechsynthesismarker/mark-swift.property.md)
  The type that describes the text.
- [var bookmarkName: String](avspeechsynthesismarker/bookmarkname.md)
  A string that represents the name of a bookmark.
- [var phoneme: String](avspeechsynthesismarker/phoneme.md)
  A string that represents a distinct sound.
- [var textRange: NSRange](avspeechsynthesismarker/textrange.md)
  The location and length of the request’s text.
- [var byteSampleOffset: Int](avspeechsynthesismarker/bytesampleoffset.md)
  The byte offset into the audio buffer.
- [AVSpeechSynthesisMarker.Mark](avspeechsynthesismarker/mark-swift.enum.md)
  Constants that describe the type of text.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias AVSpeechSynthesisProviderOutputBlock](avspeechsynthesisprovideroutputblock.md)
  A type that represents the method for sending marker information to the host.
- [var speechSynthesisOutputMetadataBlock: AVSpeechSynthesisProviderOutputBlock?](avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md)
  A block that subclasses use to send marker information to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker)*