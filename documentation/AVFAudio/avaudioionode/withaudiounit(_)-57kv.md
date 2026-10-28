# withAudioUnit(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Provides scoped access to the I/O node’s AudioUnit

**Availability**:
- macOS 27.0+

## Declaration

```swift
func withAudioUnit<R, E>(_ body: (borrowing AudioUnit?) throws(E) -> R) throws(E) -> R where E : Error
```

## Return Value

The value returned by the closure

## Discussion

This method provides thread-safe, scoped access to the underlying AudioUnit. The audio unit reference is only valid within the closure and must not be retained or accessed outside of it.

> **Throws**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives the AudioUnit instance

## See Also

### Getting the Audio Unit
- [func withAudioUnit<R, E>((borrowing AudioUnit?) throws(E) -> R) throws(E) -> R](./withaudiounit%28_%29-6i8ld.md)
  Provides scoped access to the I/O node’s AudioUnit
- [var audioUnit: AudioUnit?](./audiounit-1bqu3.md)
- [var audioUnit: AudioUnit?](./audiounit-1caha.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionode/withaudiounit(_:)-57kv)*