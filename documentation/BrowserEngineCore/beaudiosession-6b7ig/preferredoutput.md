# preferredOutput

**Framework**: BrowserEngineCore  
**Kind**: property  
**Role**: Instance Property

The output port the person sets as their preference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var preferredOutput: AVAudioSessionPortDescription? { get }
```

```objc
@property (readonly, nullable) AVAudioSessionPortDescription * preferredOutput;
```

## Discussion

The value is `nil` if a person hasn’t set a preference.

## See Also

### Managing audio output
- [var availableOutputs: [AVAudioSessionPortDescription]?](./availableoutputs.md)
  An array of output ports available for audio routing in the current session.
- [func setPreferredOutput(AVAudioSessionPortDescription?) throws](./setpreferredoutput%28_%29.md)
  Sets the preferred audio output port for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-6b7ig/preferredoutput)*