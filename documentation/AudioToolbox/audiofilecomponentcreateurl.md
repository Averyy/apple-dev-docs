# AudioFileComponentCreateURL(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
func AudioFileComponentCreateURL(_ inComponent: AudioFileComponent, _ inFileRef: CFURL, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus
```

## See Also

- [func AudioFileComponentOpenURL(AudioFileComponent, CFURL, Int8, Int32) -> OSStatus](audiofilecomponentopenurl(_:_:_:_:).md)
- [func AudioFileComponentOpenWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus](audiofilecomponentopenwithcallbacks(_:_:_:_:_:_:).md)
- [func AudioFileComponentCloseFile(AudioFileComponent) -> OSStatus](audiofilecomponentclosefile(_:).md)
- [func AudioFileComponentOptimize(AudioFileComponent) -> OSStatus](audiofilecomponentoptimize(_:).md)
- [typealias AudioFileComponent](audiofilecomponent.md)
- [typealias AudioFileComponentPropertyID](audiofilecomponentpropertyid.md)
- [typealias AudioFileComponentCreateURLProc](audiofilecomponentcreateurlproc.md)
- [typealias AudioFileComponentOpenWithCallbacksProc](audiofilecomponentopenwithcallbacksproc.md)
- [typealias AudioFileComponentOpenURLProc](audiofilecomponentopenurlproc.md)
- [typealias AudioFileComponentCloseProc](audiofilecomponentcloseproc.md)
- [typealias AudioFileComponentOptimizeProc](audiofilecomponentoptimizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcreateurl(_:_:_:_:))*