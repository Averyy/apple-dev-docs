# setPreferredIOBufferDuration(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the preferred audio I/O buffer duration.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredIOBufferDuration(_ duration: TimeInterval) throws
```

#### Discussion

This method requests a change to the I/O buffer duration. To determine whether the change has taken effect, use the [`ioBufferDuration`](avaudiosession/iobufferduration.md) property.

The audio I/O buffer duration is the number of seconds for a single audio input/output cycle. For example, with an I/O buffer duration of 0.005 s, on each audio I/O cycle:

- You receive 0.005 s of audio if obtaining input.
- You must provide 0.005 s of audio if providing output.

The typical maximum I/O buffer duration is 0.093 seconds (corresponding to 4,096 sample frames at a sample rate of 44.1 kHz). The minimum I/O buffer duration is at least 0.005 seconds (256 frames) but might be lower depending on the hardware in use.

You can set a preferred I/O buffer duration before or after activating the audio session.

## Parameters

- `duration`: The audio I/O buffer duration, in seconds, that you want to use.

## See Also

- [var ioBufferDuration: TimeInterval](avaudiosession/iobufferduration.md)
  The current I/O buffer duration, in seconds.
- [var preferredIOBufferDuration: TimeInterval](avaudiosession/preferrediobufferduration.md)
  The preferred I/O buffer duration, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferrediobufferduration(_:))*