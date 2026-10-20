# setPreferredOutput(_:)

**Framework**: BrowserEngineCore  
**Kind**: method  
**Role**: Instance Method

Sets the preferred audio output port for the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@objc
(setPreferredOutput:error:) func setPreferredOutput(_ outputPort: AVAudioSessionPortDescription?) throws
```

#### Discussion

Pass `nil` to clear the current preference and return to the system’s default output routing.

## See Also

### Managing audio output
- [var availableOutputs: Array<AVAudioSessionPortDescription>](./availableoutputs.md)
  An array of output ports available for audio routing in the current session.
- [var preferredOutput: AVAudioSessionPortDescription?](./preferredoutput.md)
  The output port the person sets as their preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q/setpreferredoutput(_:))*