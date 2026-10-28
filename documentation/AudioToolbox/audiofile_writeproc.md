# AudioFile_WriteProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A callback for writing file data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](./audiofilecreatewithurl%28_,_,_,_,_%29.md) functions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioFile_WriteProc = (UnsafeMutableRawPointer, Int64, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
typedef int (*)(void *, long long, unsigned int, const void *, unsigned int *) AudioFile_WriteProc;
```

## Return Value

A result code. See Result Codes.

## Discussion

If you named your function `MyAudioFile_WriteProc`, you would declare it like this:

### Discussion

This callback function is invoked when Audio File Services needs to write data.

## Parameters

- `inClientData`: A pointer to the client data as set in the `inClientData` parameter to [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) or[`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](./audiofileinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md).
- `inPosition`: An offset into the data from which to read.
- `requestCount`: The number of bytes to write.
- `buffer`: A pointer to the buffer containing the data to write.
- `actualCount`: Upon completion, the callback should set this to a pointer to the number of bytes successfully written.

## See Also

### Callbacks
- [typealias AudioFile_ReadProc](./audiofile_readproc.md)
  Reads audio data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) or [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](./audiofileinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md) functions.)
- [typealias AudioFile_GetSizeProc](./audiofile_getsizeproc.md)
  Gets file data size.
- [typealias AudioFile_SetSizeProc](./audiofile_setsizeproc.md)
  Sets file data size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofile_writeproc)*