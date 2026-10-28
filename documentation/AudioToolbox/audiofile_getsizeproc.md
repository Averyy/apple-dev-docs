# AudioFile_GetSizeProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Gets file data size.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioFile_GetSizeProc = (UnsafeMutableRawPointer) -> Int64
```

```c
typedef long long (*)(void *) AudioFile_GetSizeProc;
```

## Return Value

The callback should return the size of the data.

## Discussion

If you named your function `MyAudioFile_GetSizeProc`, you would declare it like this:

### Discussion

This callback gets invoked by an audio file object when it needs to get audio file data size. You pass this callback as a parameter when calling the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) and [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](./audiofileinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md) functions.

## Parameters

- `inClientData`: A pointer to the client data as set in the `inClientData` parameter to the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) or [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](./audiofileinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md) functions.

## See Also

### Callbacks
- [typealias AudioFile_ReadProc](./audiofile_readproc.md)
  Reads audio data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) or [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](./audiofileinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md) functions.)
- [typealias AudioFile_WriteProc](./audiofile_writeproc.md)
  A callback for writing file data when used in conjunction with the [`AudioFileOpenWithCallbacks(_:_:_:_:_:_:_:)`](./audiofileopenwithcallbacks%28_,_,_,_,_,_,_%29.md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](./audiofilecreatewithurl%28_,_,_,_,_%29.md) functions.
- [typealias AudioFile_SetSizeProc](./audiofile_setsizeproc.md)
  Sets file data size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofile_getsizeproc)*