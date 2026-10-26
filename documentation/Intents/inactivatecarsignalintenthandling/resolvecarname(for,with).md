# resolveCarName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the name of the user’s car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveCarName(for intent: INActivateCarSignalIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveCarName(for intent: INActivateCarSignalIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveCarNameForActivateCarSignal:(INActivateCarSignalIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the car’s name. If the app has access to more than one car, use the intent’s [`carName`](../inactivatecarsignalintent/carname.md) property to identify the correct car. If the app has access to only a single car, you can call the completion block with a `notRequired()` resolution for Swift and `resolutionResultNotRequired` for Objective-C, to indicate that the car name is not necessary.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the name of the user’s car.

## See Also

### Resolving the Intent Parameters
- [func resolveSignals(for: INActivateCarSignalIntent, with: (INCarSignalOptionsResolutionResult) -> Void)](./resolvesignals%28for,with%29.md)
  Resolves the type of signal (audible or visual).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintenthandling/resolvecarname(for:with:))*