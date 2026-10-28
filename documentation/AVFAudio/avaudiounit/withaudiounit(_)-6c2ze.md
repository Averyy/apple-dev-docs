# withAudioUnit(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Provides scoped access to the audio unit’s AudioUnit

**Availability**:
- macOS 27.0+

## Declaration

```swift
func withAudioUnit<R, E>(_ body: (borrowing AudioUnit) throws(E) -> R) throws(E) -> R where E : Error
```

## Return Value

The value returned by the closure

## Discussion

This method provides thread-safe, scoped access to the underlying AudioUnit. The audio unit reference is only valid within the closure and must not be retained or accessed outside of it.

> **Throws**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives the AudioUnit instance

## See Also

### Accessing the underlying Audio Unit
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](./withaudiounit%28_%29-66uo7.md)
  Provides scoped access to the audio unit’s AudioUnit
- [var audioUnit: AudioUnit](./audiounit-5vuo0.md)
- [var audioUnit: AudioUnit](./audiounit-7dsac.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/withaudiounit(_:)-6c2ze)*