# AVAudioSessionDelegate

**Framework**: AVFAudio  
**Kind**: protocol

A protocol that defines responses to changes in state for the audio session.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVAudioSessionDelegate : NSObjectProtocol
```

#### Overview

The delegate of an `AVAudioSession` object must adopt the `AVAudioSessionDelegate` protocol. The methods in this protocol are optional. They allow a delegate to respond to the following sorts of changes in state:

- Changes to the availability of audio input
- Audio session interruption, or end of audio session interruption

An `AVAudioSession` delegate can respond to interruptions at the audio session level. You can use this interface along with any iOS audio technology. For example, your `AVAudioSession` delegate can handle interruptions for OpenAL and audio unit playback.

When using the AVFoundation framework for recording or playback, you can also respond to interruptions at the individual recorder or player level. To do this, create audio recorder or audio player delegates using the protocols described in [`AVAudioRecorderDelegate`](avaudiorecorderdelegate.md) and [`AVAudioPlayerDelegate`](avaudioplayerdelegate.md).

## Topics

### Delegate Methods
- [func beginInterruption()](avaudiosessiondelegate/begininterruption.md)
  Called after your audio session is interrupted.
- [func endInterruption()](avaudiosessiondelegate/endinterruption.md)
  Called after your audio session interruption ends.
- [func endInterruption(withFlags: Int)](avaudiosessiondelegate/endinterruption(withflags:).md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.
- [func inputIsAvailableChanged(Bool)](avaudiosessiondelegate/inputisavailablechanged(_:).md)
  Called after the availability of audio input changes on a device.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVAudioSessionDelegate)?](avaudiosession/delegate.md)
  The delegate object for the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate)*