# AudioFileComponentInitializeWithCallbacksProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias AudioFileComponentInitializeWithCallbacksProc = (UnsafeMutableRawPointer, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus
```

## See Also

- [func AudioFileComponentInitializeWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](audiofilecomponentinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md)
- [Audio File Component Selectors](1404047-audio-file-component-selectors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentinitializewithcallbacksproc)*