# timeSignature

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The time signature of the musical composition that the audio or MIDI file contains, in a string, such as “4/4” or “7/8”.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var timeSignature: String? { get set }
```

```objc
@property (copy, nullable) NSString * timeSignature;
```

## See Also

### Describing music
- [var album: String?](./album.md)
  The title for a collection of audio media.
- [var artist: String?](./artist.md)
  The artist associated with the media.
- [var audioChannelCount: NSNumber?](./audiochannelcount.md)
  The number of channels in the audio data that the file contains.
- [var audioEncodingApplication: String?](./audioencodingapplication.md)
  The name of the application that encoded the data the audio file contains.
- [var audioSampleRate: NSNumber?](./audiosamplerate.md)
  The sample rate of the audio data the file contains, as a float value representing Hz (audio frames per second), such as 44100.0 or 22254.54.
- [var audioTrackNumber: NSNumber?](./audiotracknumber.md)
  The track number of a song or audio composition when part of an album.
- [var composer: String?](./composer.md)
  The composer of the song or audio composition that the audio file contains.
- [var keySignature: String?](./keysignature.md)
  The musical key of the song or audio composition that the file contains, such as C, Dm, or F#m.
- [var lyricist: String?](./lyricist.md)
  The lyricist or text writer for the song or audio composition that the file contains.
- [var musicalGenre: String?](./musicalgenre.md)
  The musical genre of the song or audio composition that the file contains, such as jazz, pop, rock, or classical.
- [var recordingDate: Date?](./recordingdate.md)
  The recording date of the song or composition.
- [var tempo: NSNumber?](./tempo.md)
  The tempo of the music that the audio file contains, in beats per minute.
- [var generalMIDISequence: NSNumber?](./generalmidisequence.md)
  A value that indicates whether the MIDI sequence the file contains is set up for use with a general MIDI device.
- [var musicalInstrumentCategory: String?](./musicalinstrumentcategory.md)
  The category of the instrument associated with the audio file.
- [var musicalInstrumentName: String?](./musicalinstrumentname.md)
  The name of an instrument within the context of an instrument category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/timesignature)*