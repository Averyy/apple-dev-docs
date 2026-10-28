# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides information to hand off the call to your app.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
func handle(intent: INStartVideoCallIntent, completion: @escaping @Sendable (INStartVideoCallIntentResponse) -> Void)
```

```swift
func handle(intent: INStartVideoCallIntent) async -> INStartVideoCallIntentResponse
```

```objc
- (void) handleStartVideoCall:(INStartVideoCallIntent *) intent completion:(void (^)(INStartVideoCallIntentResponse *response)) completion;
```

## Discussion

Use this method to turn control of the call over to your app. Perform any final checks and create a response object with the information needed to initiate the call in your app. Don’t try to initiate the call directly from this method. When your response object contains the [`INStartAudioCallIntentResponseCode.continueInApp`](../instartaudiocallintentresponsecode/continueinapp.md) code, Siri automatically launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response object.

## Parameters

- `intent`: The intent object containing details about the user’s request. The user has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INStartVideoCallIntentResponse`](../instartvideocallintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintenthandling/handle(intent:completion:))*