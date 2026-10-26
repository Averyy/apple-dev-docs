# resolveCarName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the car name.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveCarName(for intent: INSetSeatSettingsInCarIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveCarName(for intent: INSetSeatSettingsInCarIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveCarNameForSetSeatSettingsInCar:(INSetSeatSettingsInCarIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the name of the user’s car. If the app has access to more than one car, use the intent’s [`carName`](../insetseatsettingsincarintent/carname.md) property to identify the correct car. If the app has access to only a single car, you can call the completion block with a `notRequired()` resolution for Swift and `resolutionResultNotRequired` resolution for Objective-C, to indicate that the app doesn’t need the car name.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the name of the user’s car.

## See Also

### Resolving the Intent Parameters
- [func resolveEnableCooling(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenablecooling%28for,with%29.md)
  Resolves whether you can enable the seat cooling system.
- [func resolveEnableHeating(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenableheating%28for,with%29.md)
  Resolves whether you can enable the seat heating system.
- [func resolveEnableMassage(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenablemassage%28for,with%29.md)
  Resolves whether you can enable the seat massage system.
- [func resolveSeat(for: INSetSeatSettingsInCarIntent, with: (INCarSeatResolutionResult) -> Void)](./resolveseat%28for,with%29.md)
  Resolves the requested seat position.
- [func resolveLevel(for: INSetSeatSettingsInCarIntent, with: (INIntegerResolutionResult) -> Void)](./resolvelevel%28for,with%29.md)
  Resolves the intensity level of the requested system.
- [func resolveRelativeLevelSetting(for: INSetSeatSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./resolverelativelevelsetting%28for,with%29.md)
  Resolves the requested relative qualifier for the intensity level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintenthandling/resolvecarname(for:with:))*