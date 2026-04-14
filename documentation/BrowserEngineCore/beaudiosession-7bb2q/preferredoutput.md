# preferredOutput

**Framework**: BrowserEngineCore  
**Kind**: property

The output port the person sets as their preference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@objc
(preferredOutput) var preferredOutput: AVAudioSessionPortDescription? { get }
```

#### Discussion

The value is `nil` if a person hasn’t set a preference.

## See Also

- [var availableOutputs: Array<AVAudioSessionPortDescription>](beaudiosession-7bb2q/availableoutputs.md)
  An array of output ports available for audio routing in the current session.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](beaudiosession-7bb2q/setpreferredoutput(_:).md)
  Sets the preferred audio output port for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q/preferredoutput)*