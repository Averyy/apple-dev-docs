# resolveRelativeAudioSourceReference(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the audio source using a relative qualifier.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveRelativeAudioSourceReference(for intent: INSetAudioSourceInCarIntent, with completion: @escaping @Sendable (INRelativeReferenceResolutionResult) -> Void)
```

```swift
optional func resolveRelativeAudioSourceReference(for intent: INSetAudioSourceInCarIntent) async -> INRelativeReferenceResolutionResult
```

```objc
- (void) resolveRelativeAudioSourceReferenceForSetAudioSourceInCar:(INSetAudioSourceInCarIntent *) intent withCompletion:(void (^)(INRelativeReferenceResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the user’s request. The intent object passed to this method contains either an explicit audio source or a relative audio source, but not both. Use this method to determine whether the user selected the next or previous audio source and whether you can select that audio source in the user’s vehicle. Always strive toward a successful resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object that contains the specified [`INRelativeReference`](../inrelativereference.md) value.

## See Also

### Resolving the Intent Parameters
- [func resolveAudioSource(for: INSetAudioSourceInCarIntent, with: (INCarAudioSourceResolutionResult) -> Void)](./resolveaudiosource%28for,with%29.md)
  Resolves an explicitly selected audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintenthandling/resolverelativeaudiosourcereference(for:with:))*