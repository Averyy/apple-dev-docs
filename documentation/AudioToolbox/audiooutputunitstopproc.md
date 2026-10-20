# AudioOutputUnitStopProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioOutputUnitStopProc = (UnsafeMutableRawPointer) -> OSStatus
```

```c
typedef int (*)(void *) AudioOutputUnitStopProc;
```

## See Also

### Starting and Stopping Output
- [func AudioOutputUnitStart(AudioUnit) -> OSStatus](./audiooutputunitstart%28_%29.md)
  Starts an I/O audio unit, which in turn starts the audio unit processing graph that it is connected to.
- [func AudioOutputUnitStop(AudioUnit) -> OSStatus](./audiooutputunitstop%28_%29.md)
  Stops an I/O audio unit, which in turn stops the audio unit processing graph that it is connected to.
- [typealias AudioOutputUnitStartProc](./audiooutputunitstartproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstopproc)*