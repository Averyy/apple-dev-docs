# BEAudioSession

**Framework**: BrowserEngineCore  
**Kind**: class

An object that wraps an AV audio session to scope the browser app’s audio session control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@objc
(BEAudioSession) class BEAudioSession
```

#### Overview

This class provides a scoped interface that limits a browser-app extension’s access to the audio session. For example, an extension process can query available outputs and communicate a preferred output to the system, while the browser app’s main process retains full control over audio session configuration.

## Topics

### Initializing an audio session
- [init(audioSession: AVAudioSession)](beaudiosession-7bb2q/init(audiosession:).md)
  Initializes a browser engine audio session.
### Managing audio output
- [var availableOutputs: Array<AVAudioSessionPortDescription>](beaudiosession-7bb2q/availableoutputs.md)
  An array of output ports available for audio routing in the current session.
- [var preferredOutput: AVAudioSessionPortDescription?](beaudiosession-7bb2q/preferredoutput.md)
  The output port the person sets as their preference.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](beaudiosession-7bb2q/setpreferredoutput(_:).md)
  Sets the preferred audio output port for the session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BEAudioSession](beaudiosession-6b7ig.md)
  An object that wraps an AV audio session to scope the browser app’s audio session control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q)*