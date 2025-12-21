# BEAudioSession

**Framework**: BrowserEngineCore  
**Kind**: class

An object that represents an audio session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@objc
(BEAudioSession) class BEAudioSession
```

## Topics

### Initializers
- [init(audioSession: AVAudioSession)](beaudiosession-7bb2q/init(audiosession:).md)
  Creates a BE audio session from an  AV audio session
### Instance Properties
- [var availableOutputs: Array<AVAudioSessionPortDescription>](beaudiosession-7bb2q/availableoutputs.md)
  Gets the set of output ports that are available for routing.
- [var preferredOutput: AVAudioSessionPortDescription?](beaudiosession-7bb2q/preferredoutput.md)
  Get the preferred output port.  Will be nil if no preference has been set.
### Instance Methods
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](beaudiosession-7bb2q/setpreferredoutput(_:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q)*