# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can restore the settings from the designated profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INSetProfileInCarIntent, completion: @escaping @Sendable (INSetProfileInCarIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSetProfileInCarIntent) async -> INSetProfileInCarIntentResponse
```

```objc
- (void) confirmSetProfileInCar:(INSetProfileInCarIntent *) intent completion:(void (^)(INSetProfileInCarIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate that you can restore settings from the specified profile. For example, you might use this method to verify that you have an active connection to the vehicle and that the specified profile is valid. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to make the change.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSetProfileInCarIntentResponse`](../insetprofileincarintentresponse.md) object containing the status of whether your app is able to restore settings from the specified profile. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintenthandling/confirm(intent:completion:))*