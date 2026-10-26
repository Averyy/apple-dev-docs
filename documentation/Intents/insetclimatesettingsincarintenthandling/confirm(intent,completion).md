# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can change the climate settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INSetClimateSettingsInCarIntent, completion: @escaping @Sendable (INSetClimateSettingsInCarIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSetClimateSettingsInCarIntent) async -> INSetClimateSettingsInCarIntentResponse
```

```objc
- (void) confirmSetClimateSettingsInCar:(INSetClimateSettingsInCarIntent *) intent completion:(void (^)(INSetClimateSettingsInCarIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can change the climate settings using the given parameters. For example, you might use this method to verify that you have an active connection to the vehicle. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to make the change.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSetClimateSettingsInCarIntentResponse`](../insetclimatesettingsincarintentresponse.md) object containing the status of whether your app is able to change the climate settings. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintenthandling/confirm(intent:completion:))*