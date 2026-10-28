# resolveProfileName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the profile name in which to save any settings.

**Availability**:
- iOS 10.2+ - Deprecated in 15.0
- iPadOS 10.2+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveProfileName(for intent: INSaveProfileInCarIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveProfileName(for intent: INSaveProfileInCarIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveProfileNameForSaveProfileInCar:(INSaveProfileInCarIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to validate the profile name supplied by the user. If you don’t implement this method, SiriKit assumes that you’re able to save the profile using the specified name.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains the name of the profile you intend to use. If the name doesn’t correspond to a valid profile name, you might suggest a valid name and ask the user for confirmation.

## See Also

### Resolving the Intent Parameters
- [func resolveProfileNumber(for: INSaveProfileInCarIntent, with: (INIntegerResolutionResult) -> Void)](./resolveprofilenumber%28for,with%29.md)
  Resolves the profile index in which to save any settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintenthandling/resolveprofilename(for:with:))*