# synthesizeSpeechRequest(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) synthesizeSpeechRequest:(AVSpeechSynthesisProviderRequest *) speechRequest;
```

#### Discussion

When the synthesizer finishes generating audio buffers for the speech request, use [`AUInternalRenderBlock`](../../AudioToolbox/auinternalrenderblock.md) to report [`offlineUnitRenderAction_Complete`](../../AudioToolbox/audiounitrenderactionflags/offlineunitrenderaction_complete.md).

## Parameters

- `speechRequest`: A speech request to synthesize.

## See Also

### Rendering speech
- [class AVSpeechSynthesisProviderRequest](../avspeechsynthesisproviderrequest.md)
  An object that represents the text to synthesize and the voice to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideraudiounit/synthesizespeechrequest(_:))*