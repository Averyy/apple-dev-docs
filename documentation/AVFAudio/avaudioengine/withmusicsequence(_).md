# withMusicSequence(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Provides scoped access to the AVAudioEngine’s MusicSequence

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func withMusicSequence<R, E>(_ body: (borrowing MusicSequence?) throws(E) -> R) throws(E) -> R where E : Error
```

## Return Value

The value returned by the closure

## Discussion

This method provides thread-safe, scoped access to the MusicSequence. The MusicSequence reference is only valid within the closure and must not be retained or accessed outside of it.

> **Throws**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives a MusicSequence

## See Also

### Playing audio
- [func prepare()](./prepare%28%29.md)
  Prepares the audio engine for starting.
- [func start() throws](./start%28%29.md)
  Starts the audio engine.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func pause()](./pause%28%29.md)
  Pauses the audio engine.
- [func stop()](./stop%28%29.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](./reset%28%29.md)
  Resets all audio nodes in the audio engine.
- [var musicSequence: MusicSequence?](./musicsequence-1z47z.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/withmusicsequence(_:))*