# AudioFileStreamClose(_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFileStream`: The ID of the parser you wish to close. The parser ID is returned by the   function.

## See Also

- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](audiofilestreamopen(_:_:_:_:_:).md)
  Creates and opens a new audio file stream parser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamclose(_:))*