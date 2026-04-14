# availableOutputs

**Framework**: BrowserEngineCore  
**Kind**: property

An array of output ports available for audio routing in the current session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@objc
(availableOutputs) var availableOutputs: Array<AVAudioSessionPortDescription> { get }
```

## See Also

- [var preferredOutput: AVAudioSessionPortDescription?](beaudiosession-7bb2q/preferredoutput.md)
  The output port the person sets as their preference.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](beaudiosession-7bb2q/setpreferredoutput(_:).md)
  Sets the preferred audio output port for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q/availableoutputs)*