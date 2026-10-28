# audioSource

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The audio source to select.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var audioSource: INCarAudioSource { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCarAudioSource audioSource;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCarAudioSource audioSource;
```

## Discussion

When the user asks for a specific audio source, Siri fills this property with the requested source. If the user asked for the next or previous audio source, Siri sets this property to [`INCarAudioSource.sourceUnknown`](../incaraudiosource/sourceunknown.md).

## See Also

### Getting Details About the Audio Source to Set
- [var relativeAudioSourceReference: INRelativeReference](./relativeaudiosourcereference.md)
  The relative audio source to select.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintent/audiosource)*