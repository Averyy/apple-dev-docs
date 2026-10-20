# MIDISysExProc

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var MIDISysExProc: (UnsafeMutableRawPointer?, UnsafePointer<UInt8>, UInt32) -> Void
```

```c
void (*)(void *, const unsigned char *, unsigned int) MIDISysExProc;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/midisysexproc)*