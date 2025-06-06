# write(to:smpteResolution:replaceExisting:)

**Framework**: AVFAudio  
**Kind**: method

Creates and writes a MIDI file from the events in the sequence.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func write(to fileURL: URL, smpteResolution resolution: Int, replaceExisting replace: Bool) throws
```

#### Discussion

The framework writes only MIDI events when writing to the MIDI file. MIDI files are normally beat-based, but can also have an SMPTE (or real-time, rather than beat time) representation. The relationship between tick and quarter note for saving to a Standard MIDI File is the current value for the tempo track.

## Parameters

- `fileURL`: The URL of the file you want to write to.
- `resolution`: The relationship between tick and quarter note for saving to a Standard MIDI File. Passing zero uses the default value set using the tempo track.
- `replace`: When  , the framework overwrites an existing file at  . Otherwise, the call fails with a permission error if a file at the specified path exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/write(to:smpteresolution:replaceexisting:))*