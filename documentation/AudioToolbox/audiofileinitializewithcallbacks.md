# AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Deletes the content of an existing file and assigns callbacks to the audio file object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileInitializeWithCallbacks(_ inClientData: UnsafeMutableRawPointer, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inClientData`: A pointer to a constant passed to your callbacks. Th constant should contain any information you use to manage the state for reading data from the file.
- `inReadFunc`: A callback function invoked when the audio file object wants to read data.
- `inWriteFunc`: A callback function invoked when the audio file object wants to write data.
- `inGetSizeFunc`: A callback function invoked when the audio file object wants to know the size of the file.
- `inSetSizeFunc`: A callback function invoked when the audio file object wants to set the size of the file.
- `inFileType`: The type of audio file to initialize
- `inFormat`: The format for the audio data in the file.
- `inFlags`: Flags for creating or opening the file. Set to  .
- `outAudioFile`: On output, a pointer to the newly initialized audio file.

## See Also

- [func AudioFileOpenWithCallbacks(UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc?, AudioFile_GetSizeProc, AudioFile_SetSizeProc?, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md)
  Opens an existing file with callbacks you provide.
- [func AudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, AudioFileFlags, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](audiofilecreatewithurl(_:_:_:_:_:).md)
  Creates a new audio file, or initializes an existing file, specified by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileinitializewithcallbacks(_:_:_:_:_:_:_:_:_:))*