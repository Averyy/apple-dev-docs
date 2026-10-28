# relativeAudioSourceReference

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The relative audio source to select.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var relativeAudioSourceReference: INRelativeReference { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INRelativeReference relativeAudioSourceReference;
```

*macOS*

```objc
@property (atomic, assign, readonly) INRelativeReference relativeAudioSourceReference;
```

## Discussion

When the user asks for the next or previous audio source, Siri fills this property with an appropriate value. However, if the user asked for a specific audio source, instead of the next or previous one, Siri sets this property to [`INRelativeReference.unknown`](../inrelativereference/unknown.md).

## See Also

### Getting Details About the Audio Source to Set
- [var audioSource: INCarAudioSource](./audiosource.md)
  The audio source to select.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintent/relativeaudiosourcereference)*