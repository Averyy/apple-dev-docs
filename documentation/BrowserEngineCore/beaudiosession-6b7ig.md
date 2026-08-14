# BEAudioSession

**Framework**: BrowserEngineCore  
**Kind**: class

An object that wraps an AV audio session to scope the browser app’s audio session control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class BEAudioSession
```

#### Overview

This class provides a scoped interface that limits a browser-app extension’s access to the audio session. For example, an extension process can query available outputs and communicate a preferred output to the system, while the browser app’s main process retains full control over audio session configuration.

## Topics

### Initializing an audio session
- [init(audioSession: AVAudioSession)](beaudiosession-6b7ig/init(audiosession:).md)
  Initializes a browser engine audio session.
### Managing audio output
- [var availableOutputs: [AVAudioSessionPortDescription]?](beaudiosession-6b7ig/availableoutputs.md)
  An array of output ports available for audio routing in the current session.
- [var preferredOutput: AVAudioSessionPortDescription?](beaudiosession-6b7ig/preferredoutput.md)
  The output port the person sets as their preference.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](beaudiosession-6b7ig/setpreferredoutput(_:).md)
  Sets the preferred audio output port for the session.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class BEAudioSession](beaudiosession-7bb2q.md)
  An object that wraps an AV audio session to scope the browser app’s audio session control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-6b7ig)*