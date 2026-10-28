# resolveRadioType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the radio type.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveRadioType(for intent: INSetRadioStationIntent, with completion: @escaping @Sendable (INRadioTypeResolutionResult) -> Void)
```

```swift
optional func resolveRadioType(for intent: INSetRadioStationIntent) async -> INRadioTypeResolutionResult
```

```objc
- (void) resolveRadioTypeForSetRadioStation:(INSetRadioStationIntent *) intent withCompletion:(void (^)(INRadioTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the type of radio in the car.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with your response. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the [`INRadioType`](../inradiotype.md) value that you intend to use; otherwise, return a resolution result that offers an alternative or lets the user know that the selected value isn’t supported.

## See Also

### Resolving the Intent Parameters
- [func resolveFrequency(for: INSetRadioStationIntent, with: (INDoubleResolutionResult) -> Void)](./resolvefrequency%28for,with%29.md)
  Resolves the radio station frequency.
- [func resolveStationName(for: INSetRadioStationIntent, with: (INStringResolutionResult) -> Void)](./resolvestationname%28for,with%29.md)
  Resolves the name of the radio station.
- [func resolveChannel(for: INSetRadioStationIntent, with: (INStringResolutionResult) -> Void)](./resolvechannel%28for,with%29.md)
  Resolves the channel number for the radio station.
- [func resolvePresetNumber(for: INSetRadioStationIntent, with: (INIntegerResolutionResult) -> Void)](./resolvepresetnumber%28for,with%29.md)
  Resolves the preset number used to select the radio station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintenthandling/resolveradiotype(for:with:))*