# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles restoring settings from the designated profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INSetProfileInCarIntent, completion: @escaping @Sendable (INSetProfileInCarIntentResponse) -> Void)
```

```swift
func handle(intent: INSetProfileInCarIntent) async -> INSetProfileInCarIntentResponse
```

```objc
- (void) handleSetProfileInCar:(INSetProfileInCarIntent *) intent completion:(void (^)(INSetProfileInCarIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method should restore the settings from the specified profile. When done, execute the provided block with a response object indicating whether or not the operation was successful.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSetProfileInCarIntentResponse`](../insetprofileincarintentresponse.md) object you create to report the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintenthandling/handle(intent:completion:))*