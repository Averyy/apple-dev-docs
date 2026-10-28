# init(audioSource:relativeAudioSourceReference:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified audio source information.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(audioSource: INCarAudioSource, relativeAudioSourceReference: INRelativeReference)
```

```objc
- (instancetype) initWithAudioSource:(INCarAudioSource) audioSource relativeAudioSourceReference:(INRelativeReference) relativeAudioSourceReference;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to change the vehicle’s audio source. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths. Your test code should always specify the unknown constant for one of the parameters; don’t specify the unknown constant for both parameters.

## Parameters

- `audioSource`: The specific audio source to select. If you want to specify the next or previous audio source instead of a specific audio source, specify [`INCarAudioSource.sourceUnknown`](../incaraudiosource/sourceunknown.md) for this parameter and specify an appropriate value in the `relativeAudioSourceReference` parameter.
- `relativeAudioSourceReference`: The relative audio source to select. If you want to select a specific audio source instead, specify [`INRelativeReference.unknown`](../inrelativereference/unknown.md) for this parameter and specify an appropriate value in the `audioSource` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintent/init(audiosource:relativeaudiosourcereference:))*