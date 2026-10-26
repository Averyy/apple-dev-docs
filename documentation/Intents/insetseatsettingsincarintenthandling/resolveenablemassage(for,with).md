# resolveEnableMassage(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves whether you can enable the seat massage system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveEnableMassage(for intent: INSetSeatSettingsInCarIntent, with completion: @escaping @Sendable (INBooleanResolutionResult) -> Void)
```

```swift
optional func resolveEnableMassage(for intent: INSetSeatSettingsInCarIntent) async -> INBooleanResolutionResult
```

```objc
- (void) resolveEnableMassageForSetSeatSettingsInCar:(INSetSeatSettingsInCarIntent *) intent withCompletion:(void (^)(INBooleanResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve whether the app can enable the seat massage system.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with your response. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the originally requested value. If the intent doesn’t apply to this setting, return a result that indicates the value isn’t required.

## See Also

### Resolving the Intent Parameters
- [func resolveEnableCooling(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenablecooling%28for,with%29.md)
  Resolves whether you can enable the seat cooling system.
- [func resolveEnableHeating(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenableheating%28for,with%29.md)
  Resolves whether you can enable the seat heating system.
- [func resolveSeat(for: INSetSeatSettingsInCarIntent, with: (INCarSeatResolutionResult) -> Void)](./resolveseat%28for,with%29.md)
  Resolves the requested seat position.
- [func resolveLevel(for: INSetSeatSettingsInCarIntent, with: (INIntegerResolutionResult) -> Void)](./resolvelevel%28for,with%29.md)
  Resolves the intensity level of the requested system.
- [func resolveRelativeLevelSetting(for: INSetSeatSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./resolverelativelevelsetting%28for,with%29.md)
  Resolves the requested relative qualifier for the intensity level.
- [func resolveCarName(for: INSetSeatSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the car name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintenthandling/resolveenablemassage(for:with:))*