# AVSpeechSynthesisMarker

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVSpeechSynthesisMarker : NSObject
```

## Topics

### Creating a marker
- [init(markerType: AVSpeechSynthesisMarker.Mark, forTextRange: NSRange, atByteSampleOffset: Int)](./avspeechsynthesismarker/init%28markertype,fortextrange,atbytesampleoffset%29.md)
  Creates a marker with a type and location of the request’s text.
- [init(wordRange: NSRange, atByteSampleOffset: Int)](./avspeechsynthesismarker/init%28wordrange,atbytesampleoffset%29.md)
  Creates a word marker with a range of the word and offset into the audio buffer.
- [init(sentenceRange: NSRange, atByteSampleOffset: Int)](./avspeechsynthesismarker/init%28sentencerange,atbytesampleoffset%29.md)
  Creates a sentence marker with a range of the sentence and offset into the audio buffer.
- [init(paragraphRange: NSRange, atByteSampleOffset: Int)](./avspeechsynthesismarker/init%28paragraphrange,atbytesampleoffset%29.md)
  Creates a paragraph marker with a range of the paragraph and offset into the audio buffer.
- [init(phonemeString: String, atByteSampleOffset: Int)](./avspeechsynthesismarker/init%28phonemestring,atbytesampleoffset%29.md)
  Creates a phoneme marker with a range of the phoneme and offset into the audio buffer.
- [init(bookmarkName: String, atByteSampleOffset: Int)](./avspeechsynthesismarker/init%28bookmarkname,atbytesampleoffset%29.md)
  Creates a bookmark marker with a name and offset into the audio buffer.
### Inspecting a marker
- [var mark: AVSpeechSynthesisMarker.Mark](./avspeechsynthesismarker/mark-swift.property.md)
  The type that describes the text.
- [var bookmarkName: String](./avspeechsynthesismarker/bookmarkname.md)
  A string that represents the name of a bookmark.
- [var phoneme: String](./avspeechsynthesismarker/phoneme.md)
  A string that represents a distinct sound.
- [var textRange: NSRange](./avspeechsynthesismarker/textrange.md)
  The location and length of the request’s text.
- [var byteSampleOffset: Int](./avspeechsynthesismarker/bytesampleoffset.md)
  The byte offset into the audio buffer.
- [AVSpeechSynthesisMarker.Mark](./avspeechsynthesismarker/mark-swift.enum.md)
  Constants that describe the type of text.
### Initializers
- [init?(coder: NSCoder)](./avspeechsynthesismarker/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Directing speech output
- [var usesApplicationAudioSession: Bool](./avspeechsynthesizer/usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](./avspeechsynthesizer/mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](./avspeechsynthesizer/outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](./avspeechsynthesizer/write%28_,tobuffercallback%29.md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](./avspeechsynthesizer/buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](./avspeechsynthesizer/write%28_,tobuffercallback,tomarkercallback%29.md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](./avspeechsynthesizer/markercallback.md)
  A type that defines a callback that receives speech markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker)*