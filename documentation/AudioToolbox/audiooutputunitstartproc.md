# AudioOutputUnitStartProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioOutputUnitStartProc = (UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioOutputUnitStart(AudioUnit) -> OSStatus](audiooutputunitstart(_:).md)
  Starts an I/O audio unit, which in turn starts the audio unit processing graph that it is connected to.
- [func AudioOutputUnitStop(AudioUnit) -> OSStatus](audiooutputunitstop(_:).md)
  Stops an I/O audio unit, which in turn stops the audio unit processing graph that it is connected to.
- [typealias AudioOutputUnitStopProc](audiooutputunitstopproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartproc)*