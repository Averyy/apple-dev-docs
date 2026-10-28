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
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: INStartAudioCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
func handle(intent: INStartAudioCallIntent, completion: @escaping @Sendable (INStartAudioCallIntentResponse) -> Void)
```

```swift
func handle(intent: INStartAudioCallIntent) async -> INStartAudioCallIntentResponse
```

```objc
- (void) handleStartAudioCall:(INStartAudioCallIntent *) intent completion:(void (^)(INStartAudioCallIntentResponse *response)) completion;
```

## Discussion

Use this method to turn control of the call over to your app. Perform any final checks and create a response object with the information needed to initiate the call in your app. Don’t try to initiate the call directly from this method. When your response object contains the [`INStartAudioCallIntentResponseCode.continueInApp`](../instartaudiocallintentresponsecode/continueinapp.md) code, Siri automatically launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response object.

## Parameters

- `intent`: The intent object containing details about the user’s request. The user has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INStartAudioCallIntentResponse`](../instartaudiocallintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintenthandling/handle(intent:completion:))*