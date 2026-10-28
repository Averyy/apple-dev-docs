# resolveSignals(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the type of signal (audible or visual).

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveSignals(for intent: INActivateCarSignalIntent, with completion: @escaping @Sendable (INCarSignalOptionsResolutionResult) -> Void)
```

```swift
optional func resolveSignals(for intent: INActivateCarSignalIntent) async -> INCarSignalOptionsResolutionResult
```

```objc
- (void) resolveSignalsForActivateCarSignal:(INActivateCarSignalIntent *) intent withCompletion:(void (^)(INCarSignalOptionsResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify the requested signal type (audible or visual). For the complete list of possible signals, see [`INCarSignalOptions`](../incarsignaloptions.md).

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object that specifies the requested signal types.

## See Also

### Resolving the Intent Parameters
- [func resolveCarName(for: INActivateCarSignalIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the name of the user’s car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintenthandling/resolvesignals(for:with:))*