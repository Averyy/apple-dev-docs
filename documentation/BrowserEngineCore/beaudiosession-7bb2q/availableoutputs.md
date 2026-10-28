# availableOutputs

**Framework**: BrowserEngineCore  
**Kind**: property  
**Role**: Instance Property

An array of output ports available for audio routing in the current session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@objc(availableOutputs)
var availableOutputs: Array<AVAudioSessionPortDescription> { get }
```

## See Also

### Managing audio output
- [var preferredOutput: AVAudioSessionPortDescription?](./preferredoutput.md)
  The output port the person sets as their preference.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](./setpreferredoutput%28_%29.md)
  Sets the preferred audio output port for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q/availableoutputs)*