# AudioFileOpenURL(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Open an existing audio file specified by a URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileOpenURL(_ inFileRef: CFURL, _ inPermissions: AudioFilePermissions, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inFileRef`: The URL of an existing audio file.
- `inPermissions`: The read-write permissions you want to assign to the file. Use the permission constants in  .
- `inFileTypeHint`: A hint for the file type of the designated file. For files without filename extensions and with types not easily or uniquely determined from the data (such as ADTS or AC3), use this hint to indicate the file type. Otherwise,  pass  . Only use this hint in macOS versions 10.3.1 or greater. In all earlier versions, any attempt to open these files fails.
- `outAudioFile`: On output, a pointer to the newly opened audio file.

## See Also

- [func AudioFileOpenWithCallbacks(UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc?, AudioFile_GetSizeProc, AudioFile_SetSizeProc?, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md)
  Opens an existing file with callbacks you provide.
- [func AudioFileClose(AudioFileID) -> OSStatus](audiofileclose(_:).md)
  Closes an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileopenurl(_:_:_:_:))*