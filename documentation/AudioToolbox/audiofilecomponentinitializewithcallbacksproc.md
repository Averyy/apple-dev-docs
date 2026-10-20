# AudioFileComponentInitializeWithCallbacksProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentInitializeWithCallbacksProc = (UnsafeMutableRawPointer, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus
```

```c
typedef int (*)(void *, void *, int (*)(void *, long long, unsigned int, void *, unsigned int *), int (*)(void *, long long, unsigned int, const void *, unsigned int *), long long (*)(void *), int (*)(void *, long long), unsigned int, const struct AudioStreamBasicDescription *, unsigned int) AudioFileComponentInitializeWithCallbacksProc;
```

## See Also

### Configuring the Callbacks
- [func AudioFileComponentInitializeWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](./audiofilecomponentinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md)
- [Audio File Component Selectors](./api-1404047-audio-file-component-selectors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentinitializewithcallbacksproc)*