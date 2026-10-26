# resolveDefaultProfile(forSetProfileInCar:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves whether the profile can become the default profile.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
optional func resolveDefaultProfile(forSetProfileInCar intent: INSetProfileInCarIntent, with completion: @escaping @Sendable (INBooleanResolutionResult) -> Void)
```

*Mac Catalyst, visionOS*

```swift
optional func resolveDefaultProfile(forSetProfileInCar intent: INSetProfileInCarIntent) async -> INBooleanResolutionResult
```

```objc
- (void) resolveDefaultProfileForSetProfileInCar:(INSetProfileInCarIntent *) intent withCompletion:(void (^)(INBooleanResolutionResult *resolutionResult)) completion;
```

#### Discussion

If you don’t allow the specified profile to become the default, return an unsupported resolution result.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with your response. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains the original Boolean value.

## See Also

### Resolving the Intent Parameters
- [func resolveProfileNumber(for: INSetProfileInCarIntent, with: (INIntegerResolutionResult) -> Void)](./resolveprofilenumber%28for,with%29.md)
  Resolves the profile index from which to restore any settings.
- [func resolveProfileName(for: INSetProfileInCarIntent, with: (INStringResolutionResult) -> Void)](./resolveprofilename%28for,with%29.md)
  Resolves the profile name from which to retrieve settings.
- [func resolveCarName(for: INSetProfileInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the car name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintenthandling/resolvedefaultprofile(forsetprofileincar:with:))*