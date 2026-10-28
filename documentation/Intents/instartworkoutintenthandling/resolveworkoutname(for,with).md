# resolveWorkoutName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the workout name selected by the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveWorkoutName(for intent: INStartWorkoutIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveWorkoutName(for intent: INStartWorkoutIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveWorkoutNameForStartWorkout:(INStartWorkoutIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

## Discussion

This method resolves the workout name. Use it to validate the user-supplied workout name. If you don’t implement this method, SiriKit assumes that you’re able to start the requested workout with the specified name.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For a successful resolution, create a resolution result that includes the name of the workout you plan to start.

## See Also

### Resolving the Intent Parameters
- [func resolveGoalValue(for: INStartWorkoutIntent, with: (INDoubleResolutionResult) -> Void)](./resolvegoalvalue%28for,with%29.md)
  Resolves the numerical goal of a user’s workout.
- [func resolveWorkoutGoalUnitType(for: INStartWorkoutIntent, with: (INWorkoutGoalUnitTypeResolutionResult) -> Void)](./resolveworkoutgoalunittype%28for,with%29.md)
  Resolves the units for the user’s workout goal.
- [func resolveWorkoutLocationType(for: INStartWorkoutIntent, with: (INWorkoutLocationTypeResolutionResult) -> Void)](./resolveworkoutlocationtype%28for,with%29.md)
  Resolves the location type of a user’s workout.
- [func resolveIsOpenEnded(for: INStartWorkoutIntent, with: (INBooleanResolutionResult) -> Void)](./resolveisopenended%28for,with%29.md)
  Resolves whether the user’s workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintenthandling/resolveworkoutname(for:with:))*