# AudioOutputUnitStop(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Stops an I/O audio unit, which in turn stops the audio unit processing graph that it is connected to.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioOutputUnitStop(_ ci: AudioUnit) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `ci`: The I/O audio unit to stop.

## See Also

- [func AudioOutputUnitStart(AudioUnit) -> OSStatus](audiooutputunitstart(_:).md)
  Starts an I/O audio unit, which in turn starts the audio unit processing graph that it is connected to.
- [typealias AudioOutputUnitStartProc](audiooutputunitstartproc.md)
- [typealias AudioOutputUnitStopProc](audiooutputunitstopproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstop(_:))*