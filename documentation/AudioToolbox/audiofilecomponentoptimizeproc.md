# AudioFileComponentOptimizeProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias AudioFileComponentOptimizeProc = (UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentCreateURL(AudioFileComponent, CFURL, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](audiofilecomponentcreateurl(_:_:_:_:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentoptimizeproc)*