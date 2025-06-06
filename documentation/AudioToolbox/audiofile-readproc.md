# AudioFile_ReadProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Reads audio data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) or [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](audiofileinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md) functions.)

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioFile_ReadProc = (UnsafeMutableRawPointer, Int64, UInt32, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

If you named your function `MyAudioFile_ReadProc`, you would declare it like this:

##### Discussion

This callback function is called when Audio File Services needs to read data.

## Parameters

- `inClientData`: A pointer to the client data as set in the   parameter to   or  .
- `inPosition`: An offset into the data from which to read.
- `requestCount`: The number of bytes to read.
- `buffer`: A pointer to the buffer in which to put the data read.
- `actualCount`: On output, the callback should set this parameter to a pointer to the number of bytes successfully read.

## See Also

- [typealias AudioFile_WriteProc](audiofile_writeproc.md)
  A callback for writing file data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](audiofileopenwithcallbacks(_:_:_:_:_:_:_:).md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](audiofilecreatewithurl(_:_:_:_:_:).md) functions.
- [typealias AudioFile_GetSizeProc](audiofile_getsizeproc.md)
  Gets file data size.
- [typealias AudioFile_SetSizeProc](audiofile_setsizeproc.md)
  Sets file data size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofile_readproc)*