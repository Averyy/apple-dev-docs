# setPreferredOutput(_:)

**Framework**: BrowserEngineCore  
**Kind**: method

Sets the preferred audio output port for the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func setPreferredOutput(_ outPort: AVAudioSessionPortDescription?) throws
```

#### Discussion

Pass `nil` to clear the current preference and return to the system’s default output routing.

## See Also

- [var availableOutputs: [AVAudioSessionPortDescription]?](beaudiosession-6b7ig/availableoutputs.md)
  An array of output ports available for audio routing in the current session.
- [var preferredOutput: AVAudioSessionPortDescription?](beaudiosession-6b7ig/preferredoutput.md)
  The output port the person sets as their preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-6b7ig/setpreferredoutput(_:))*