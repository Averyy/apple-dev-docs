# musicalInstrumentCategory

**Framework**: Core Spotlight  
**Kind**: property

The category of the instrument associated with the audio file.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var musicalInstrumentCategory: String? { get set }
```

#### Discussion

A file should specify an associated instrument (note that you can use “Other Instrument” to specify an unknown instrument). In some categories, you can use instrument names to provide a more detailed instrument definition. For example, the Keyboards category lets you include instrument names such as Piano or Organ.

## See Also

- [var album: String?](cssearchableitemattributeset/album.md)
  The title for a collection of audio media.
- [var artist: String?](cssearchableitemattributeset/artist.md)
  The artist associated with the media.
- [var audioChannelCount: NSNumber?](cssearchableitemattributeset/audiochannelcount.md)
  The number of channels in the audio data that the file contains.
- [var audioEncodingApplication: String?](cssearchableitemattributeset/audioencodingapplication.md)
  The name of the application that encoded the data the audio file contains.
- [var audioSampleRate: NSNumber?](cssearchableitemattributeset/audiosamplerate.md)
  The sample rate of the audio data the file contains, as a float value representing Hz (audio frames per second), such as 44100.0 or 22254.54.
- [var audioTrackNumber: NSNumber?](cssearchableitemattributeset/audiotracknumber.md)
  The track number of a song or audio composition when part of an album.
- [var composer: String?](cssearchableitemattributeset/composer.md)
  The composer of the song or audio composition that the audio file contains.
- [var keySignature: String?](cssearchableitemattributeset/keysignature.md)
  The musical key of the song or audio composition that the file contains, such as C, Dm, or F#m.
- [var lyricist: String?](cssearchableitemattributeset/lyricist.md)
  The lyricist or text writer for the song or audio composition that the file contains.
- [var musicalGenre: String?](cssearchableitemattributeset/musicalgenre.md)
  The musical genre of the song or audio composition that the file contains, such as jazz, pop, rock, or classical.
- [var recordingDate: Date?](cssearchableitemattributeset/recordingdate.md)
  The recording date of the song or composition.
- [var tempo: NSNumber?](cssearchableitemattributeset/tempo.md)
  The tempo of the music that the audio file contains, in beats per minute.
- [var timeSignature: String?](cssearchableitemattributeset/timesignature.md)
  The time signature of the musical composition that the audio or MIDI file contains, in a string, such as “4/4” or “7/8”.
- [var generalMIDISequence: NSNumber?](cssearchableitemattributeset/generalmidisequence.md)
  A value that indicates whether the MIDI sequence the file contains is set up for use with a general MIDI device.
- [var musicalInstrumentName: String?](cssearchableitemattributeset/musicalinstrumentname.md)
  The name of an instrument within the context of an instrument category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/musicalinstrumentcategory)*