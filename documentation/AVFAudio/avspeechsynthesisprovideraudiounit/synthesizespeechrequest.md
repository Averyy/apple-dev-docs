# synthesizeSpeechRequest(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the text to synthesize and the voice to use.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func synthesizeSpeechRequest(_ speechRequest: AVSpeechSynthesisProviderRequest)
```

#### Discussion

When the synthesizer finishes generating audio buffers for the speech request, use [`AUInternalRenderBlock`](https://developer.apple.com/documentation/AudioToolbox/AUInternalRenderBlock) to report [`offlineUnitRenderAction_Complete`](https://developer.apple.com/documentation/AudioToolbox/AudioUnitRenderActionFlags/offlineUnitRenderAction_Complete).

## Parameters

- `speechRequest`: A speech request to synthesize.

## See Also

- [class AVSpeechSynthesisProviderRequest](avspeechsynthesisproviderrequest.md)
  An object that represents the text to synthesize and the voice to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideraudiounit/synthesizespeechrequest(_:))*