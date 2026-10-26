# resolveIsOpenEnded(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves whether the user’s workout is open ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveIsOpenEnded(for intent: INStartWorkoutIntent, with completion: @escaping @Sendable (INBooleanResolutionResult) -> Void)
```

```swift
optional func resolveIsOpenEnded(for intent: INStartWorkoutIntent) async -> INBooleanResolutionResult
```

```objc
- (void) resolveIsOpenEndedForStartWorkout:(INStartWorkoutIntent *) intent withCompletion:(void (^)(INBooleanResolutionResult *resolutionResult)) completion;
```

#### Discussion

This method resolves whether the workout is open ended. If you don’t implement this method, SiriKit assumes that you’re able to start either an open ended or fixed goal workout.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing information about your proposed resolution. For a successful resolution, create a resolution result that includes the Boolean value indicating whether you plan to start the workout with an open-ended or fixed goal. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INStartWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveworkoutname%28for,with%29.md)
  Resolves the workout name selected by the user.
- [func resolveGoalValue(for: INStartWorkoutIntent, with: (INDoubleResolutionResult) -> Void)](./resolvegoalvalue%28for,with%29.md)
  Resolves the numerical goal of a user’s workout.
- [func resolveWorkoutGoalUnitType(for: INStartWorkoutIntent, with: (INWorkoutGoalUnitTypeResolutionResult) -> Void)](./resolveworkoutgoalunittype%28for,with%29.md)
  Resolves the units for the user’s workout goal.
- [func resolveWorkoutLocationType(for: INStartWorkoutIntent, with: (INWorkoutLocationTypeResolutionResult) -> Void)](./resolveworkoutlocationtype%28for,with%29.md)
  Resolves the location type of a user’s workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintenthandling/resolveisopenended(for:with:))*