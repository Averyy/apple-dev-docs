# AudioFileClose(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Closes an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileClose(_ inAudioFile: AudioFileID) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFile`: The file you want to close.

## See Also

- [func AudioFileOpenURL(CFURL, AudioFilePermissions, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileopenurl(_:_:_:_:).md)
  Open an existing audio file specified by a URL.
- [func AudioFileOpenWithCallbacks(UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc?, AudioFile_GetSizeProc, AudioFile_SetSizeProc?, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md)
  Opens an existing file with callbacks you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileclose(_:))*