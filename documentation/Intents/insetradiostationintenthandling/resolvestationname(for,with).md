# resolveStationName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the name of the radio station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveStationName(for intent: INSetRadioStationIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveStationName(for intent: INSetRadioStationIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveStationNameForSetRadioStation:(INSetRadioStationIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the name of the radio station. Use this method to set the radio to the station associated with the resolved name.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with your response. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the name of the radio station, if any. If the radio station isn’t relevant for your system, you can also create a resolution result indicating that the value isn’t required.

## See Also

### Resolving the Intent Parameters
- [func resolveRadioType(for: INSetRadioStationIntent, with: (INRadioTypeResolutionResult) -> Void)](./resolveradiotype%28for,with%29.md)
  Resolves the radio type.
- [func resolveFrequency(for: INSetRadioStationIntent, with: (INDoubleResolutionResult) -> Void)](./resolvefrequency%28for,with%29.md)
  Resolves the radio station frequency.
- [func resolveChannel(for: INSetRadioStationIntent, with: (INStringResolutionResult) -> Void)](./resolvechannel%28for,with%29.md)
  Resolves the channel number for the radio station.
- [func resolvePresetNumber(for: INSetRadioStationIntent, with: (INIntegerResolutionResult) -> Void)](./resolvepresetnumber%28for,with%29.md)
  Resolves the preset number used to select the radio station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintenthandling/resolvestationname(for:with:))*