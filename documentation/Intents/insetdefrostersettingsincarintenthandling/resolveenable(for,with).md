# resolveEnable(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves whether you can enable or disable the defroster setting.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveEnable(for intent: INSetDefrosterSettingsInCarIntent, with completion: @escaping @Sendable (INBooleanResolutionResult) -> Void)
```

```swift
optional func resolveEnable(for intent: INSetDefrosterSettingsInCarIntent) async -> INBooleanResolutionResult
```

```objc
- (void) resolveEnableForSetDefrosterSettingsInCar:(INSetDefrosterSettingsInCarIntent *) intent withCompletion:(void (^)(INBooleanResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve whether the app can enable the defrost.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value reflects the value chosen by the user. If you can’t set the defroster to the specified value, specify a resolution result indicating whether you require confirmation from the user before making the change or whether the change isn’t possible.

## See Also

### Resolving the Intent Parameters
- [func resolveDefroster(for: INSetDefrosterSettingsInCarIntent, with: (INCarDefrosterResolutionResult) -> Void)](./resolvedefroster%28for,with%29.md)
  Resolves which defroster to change.
- [func resolveCarName(for: INSetDefrosterSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the car name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintenthandling/resolveenable(for:with:))*