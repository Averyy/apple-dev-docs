# withAudioUnit(_:)

**Framework**: AVFAudio  
**Kind**: method

Provides scoped access to the audio unit’s AudioUnit

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func withAudioUnit<R, E>(_ body: (borrowing AudioUnit) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The value returned by the closure

#### Discussion

This method provides thread-safe, scoped access to the underlying AudioUnit. The audio unit reference is only valid within the closure and must not be retained or accessed outside of it.

> **Note**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives the AudioUnit instance


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/withaudiounit(_:)-6c2ze)*