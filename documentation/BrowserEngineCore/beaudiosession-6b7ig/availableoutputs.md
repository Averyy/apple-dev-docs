# availableOutputs

**Framework**: BrowserEngineCore  
**Kind**: property

An array of output ports available for audio routing in the current session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var availableOutputs: [AVAudioSessionPortDescription]? { get }
```

## See Also

- [var preferredOutput: AVAudioSessionPortDescription?](beaudiosession-6b7ig/preferredoutput.md)
  The output port the person sets as their preference.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](beaudiosession-6b7ig/setpreferredoutput(_:).md)
  Sets the preferred audio output port for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-6b7ig/availableoutputs)*