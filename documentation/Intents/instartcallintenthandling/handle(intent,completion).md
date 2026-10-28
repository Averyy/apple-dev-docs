# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles handing off the call to your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func handle(intent: INStartCallIntent, completion: @escaping @Sendable (INStartCallIntentResponse) -> Void)
```

```swift
func handle(intent: INStartCallIntent) async -> INStartCallIntentResponse
```

```objc
- (void) handleStartCall:(INStartCallIntent *) intent completion:(void (^)(INStartCallIntentResponse *response)) completion;
```

## Discussion

Use this method to transfer control of the call to your app. Perform any final checks and create a response object with the information needed to initiate the call in your app. Don’t try to initiate the call directly from this method. When your response object contains the [`INStartAudioCallIntentResponseCode.continueInApp`](../instartaudiocallintentresponsecode/continueinapp.md) code, Siri automatically launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response object.

## Parameters

- `intent`: The intent object that contains details about the user’s request. The information in this object has already been resolved by the user.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INStartAudioCallIntentResponse`](../instartaudiocallintentresponse.md) object that contains the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintenthandling/handle(intent:completion:))*