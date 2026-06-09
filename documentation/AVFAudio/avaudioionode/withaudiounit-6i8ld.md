# withAudioUnit(_:)

**Framework**: AVFAudio  
**Kind**: method

Provides scoped access to the I/O node’s AudioUnit

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withAudioUnit<R, E>(_ body: (borrowing AudioUnit?) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The value returned by the closure

#### Discussion

This method provides thread-safe, scoped access to the underlying AudioUnit. The audio unit reference is only valid within the closure and must not be retained or accessed outside of it.

> **Note**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives the AudioUnit instance


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionode/withaudiounit(_:)-6i8ld)*