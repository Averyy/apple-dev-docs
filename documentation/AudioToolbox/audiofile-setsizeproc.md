# AudioFile_SetSizeProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Sets file data size.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioFile_SetSizeProc = (UnsafeMutableRawPointer, Int64) -> OSStatus
```

#### Return Value

The callback should return the size of the data.

#### Discussion

If you named your function `MyAudioFile_SetSizeProc`, you would declare it like this:

##### Discussion

This callback gets invoked by an audio file object when it needs to set audio file data size. You pass this callback as a parameter when calling the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) and [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](audiofileinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md) functions.

## Parameters

- `inClientData`: A pointer to the client data as set in the   parameter to the   or   functions.

## See Also

- [typealias AudioFile_ReadProc](audiofile_readproc.md)
  Reads audio data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) or [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](audiofileinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md) functions.)
- [typealias AudioFile_WriteProc](audiofile_writeproc.md)
  A callback for writing file data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](audiofilecreatewithurl(_:_:_:_:_:).md) functions.
- [typealias AudioFile_GetSizeProc](audiofile_getsizeproc.md)
  Gets file data size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofile_setsizeproc)*