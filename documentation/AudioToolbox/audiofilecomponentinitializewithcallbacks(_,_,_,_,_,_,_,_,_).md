# AudioFileComponentInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentInitializeWithCallbacks(_ inComponent: AudioFileComponent, _ inClientData: UnsafeMutableRawPointer, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: UInt32, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus
```

```c
extern OSStatus AudioFileComponentInitializeWithCallbacks(AudioFileComponent inComponent, void *inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc, UInt32 inFileType, const AudioStreamBasicDescription *inFormat, UInt32 inFlags);
```

## See Also

### Configuring the Callbacks
- [Audio File Component Selectors](./api-1404047-audio-file-component-selectors.md)
- [typealias AudioFileComponentInitializeWithCallbacksProc](./audiofilecomponentinitializewithcallbacksproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentinitializewithcallbacks(_:_:_:_:_:_:_:_:_:))*