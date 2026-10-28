# AudioFileStreamClose(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Closes and deallocates the specified audio file stream parser.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamClose(_ inAudioFileStream: AudioFileStreamID) -> OSStatus
```

```c
extern OSStatus AudioFileStreamClose(AudioFileStreamID inAudioFileStream);
```

## Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFileStream`: The ID of the parser you wish to close. The parser ID is returned by the [`AudioFileStreamOpen(_:_:_:_:_:)`](./audiofilestreamopen%28_,_,_,_,_%29.md) function.

## See Also

### Related Documentation
- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](./audiofilestreamopen%28_,_,_,_,_%29.md)
  Creates and opens a new audio file stream parser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamclose(_:))*