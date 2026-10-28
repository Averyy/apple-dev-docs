# resolveWorkoutGoalUnitType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the units for the user’s workout goal.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveWorkoutGoalUnitType(for intent: INStartWorkoutIntent, with completion: @escaping @Sendable (INWorkoutGoalUnitTypeResolutionResult) -> Void)
```

```swift
optional func resolveWorkoutGoalUnitType(for intent: INStartWorkoutIntent) async -> INWorkoutGoalUnitTypeResolutionResult
```

```objc
- (void) resolveWorkoutGoalUnitTypeForStartWorkout:(INStartWorkoutIntent *) intent withCompletion:(void (^)(INWorkoutGoalUnitTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

This method resolves the units for the user’s goal. Use it to validate the units of the user-supplied workout goal. If you don’t implement this method, SiriKit assumes that you’re able to start the workout with the specified goal.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For a successful resolution, create a resolution result that includes the [`INWorkoutGoalUnitType`](../inworkoutgoalunittype.md) constant you plan to use for the workout goal.

## See Also

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INStartWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveworkoutname%28for,with%29.md)
  Resolves the workout name selected by the user.
- [func resolveGoalValue(for: INStartWorkoutIntent, with: (INDoubleResolutionResult) -> Void)](./resolvegoalvalue%28for,with%29.md)
  Resolves the numerical goal of a user’s workout.
- [func resolveWorkoutLocationType(for: INStartWorkoutIntent, with: (INWorkoutLocationTypeResolutionResult) -> Void)](./resolveworkoutlocationtype%28for,with%29.md)
  Resolves the location type of a user’s workout.
- [func resolveIsOpenEnded(for: INStartWorkoutIntent, with: (INBooleanResolutionResult) -> Void)](./resolveisopenended%28for,with%29.md)
  Resolves whether the user’s workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintenthandling/resolveworkoutgoalunittype(for:with:))*