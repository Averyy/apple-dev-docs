# resolveAudioSource(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves an explicitly selected audio source.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveAudioSource(for intent: INSetAudioSourceInCarIntent, with completion: @escaping @Sendable (INCarAudioSourceResolutionResult) -> Void)
```

```swift
optional func resolveAudioSource(for intent: INSetAudioSourceInCarIntent) async -> INCarAudioSourceResolutionResult
```

```objc
- (void) resolveAudioSourceForSetAudioSourceInCar:(INSetAudioSourceInCarIntent *) intent withCompletion:(void (^)(INCarAudioSourceResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the user’s request. The intent object passed to this method contains either an explicit audio source or a relative audio source, but not both. Use this method to determine whether the specified audio source is selectable in the user’s vehicle. Always strive toward a successful resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object that contains the specified [`INCarAudioSource`](../incaraudiosource.md) value. If the vehicle doesn’t support the requested audio source, specify a comparable audio source or specify a different audio source and ask the user to confirm the choice.

## See Also

### Resolving the Intent Parameters
- [func resolveRelativeAudioSourceReference(for: INSetAudioSourceInCarIntent, with: (INRelativeReferenceResolutionResult) -> Void)](./resolverelativeaudiosourcereference%28for,with%29.md)
  Resolves the audio source using a relative qualifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintenthandling/resolveaudiosource(for:with:))*